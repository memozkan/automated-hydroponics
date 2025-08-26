#!/usr/bin/env python3
"""Read hydroponic sensor data from a serial port and optionally POST to a remote server.

This script expects the Arduino sketch to print space-separated values in the
order: N light_value ph_value ec_value. It will parse the data, display it on
stdout and, if an HTTP endpoint is provided, send the measurements as JSON.
"""
import argparse
import json
import sys
import time
from typing import Optional

try:
    import serial  # type: ignore
except Exception:  # pragma: no cover
    serial = None  # pyserial may not be installed on this system

try:
    import requests  # type: ignore
except Exception:  # pragma: no cover
    requests = None


def read_loop(port: str, baud: int, endpoint: Optional[str]) -> None:
    if serial is None:
        raise RuntimeError("pyserial is required to read from the serial port")

    with serial.Serial(port, baudrate=baud, timeout=1) as ser:
        while True:
            line = ser.readline().decode().strip()
            if not line:
                continue
            parts = line.split()
            if len(parts) < 4:
                continue
            _, light, ph, ec = parts[:4]
            data = {"light": float(light), "ph": float(ph), "ec": float(ec)}
            print(json.dumps(data))
            if endpoint and requests is not None:
                try:
                    requests.post(endpoint, json=data, timeout=5)
                except Exception as exc:  # pragma: no cover
                    print(f"Failed to post data: {exc}", file=sys.stderr)
            time.sleep(1)


def main() -> None:
    parser = argparse.ArgumentParser(description="Monitor hydroponic sensor data")
    parser.add_argument("--port", default="/dev/ttyUSB0", help="Serial port path")
    parser.add_argument("--baud", type=int, default=9600, help="Serial baud rate")
    parser.add_argument(
        "--endpoint",
        help="HTTP endpoint to post JSON data (optional)",
    )
    args = parser.parse_args()
    try:
        read_loop(args.port, args.baud, args.endpoint)
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()
