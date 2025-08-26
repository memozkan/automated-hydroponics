#!/usr/bin/env python3
"""Seri porttan hidroponik sensör verilerini okuyup isteğe bağlı olarak uzak bir sunucuya POST eder.

Bu betik, Arduino skeç'inin `N light_value ph_value ec_value` sırasıyla boşlukla ayrılmış
değerler yazmasını bekler. Verileri ayrıştırır, stdout'a gösterir ve bir HTTP uç noktası
sağlanmışsa ölçümleri JSON olarak gönderir.
"""
import argparse
import json
import sys
import time
from typing import Optional

try:
    import serial  # type: ignore
except Exception:  # pragma: no cover
    serial = None  # pyserial bu sistemde kurulu olmayabilir

try:
    import requests  # type: ignore
except Exception:  # pragma: no cover
    requests = None


def read_loop(port: str, baud: int, endpoint: Optional[str]) -> None:
    if serial is None:
        raise RuntimeError("seri porttan okumak için pyserial gereklidir")

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
                    print(f"Veri gönderilemedi: {exc}", file=sys.stderr)
            time.sleep(1)


def main() -> None:
    parser = argparse.ArgumentParser(description="Hidroponik sensör verilerini izle")
    parser.add_argument("--port", default="/dev/ttyUSB0", help="Seri port yolu")
    parser.add_argument("--baud", type=int, default=9600, help="Seri baud hızı")
    parser.add_argument(
        "--endpoint",
        help="JSON verisini POST etmek için HTTP uç noktası (isteğe bağlı)",
    )
    args = parser.parse_args()
    try:
        read_loop(args.port, args.baud, args.endpoint)
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()

