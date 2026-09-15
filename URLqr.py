from datetime import datetime
from pathlib import Path
from urllib.parse import urlparse

try:
    import qrcode
except ModuleNotFoundError:
    print('Missing package. Install it with: python -m pip install "qrcode[pil]"')
    raise SystemExit(1)


def ask_for_url():
    while True:
        url = input("Enter the URL: ").strip()

        if not url:
            print("The URL cannot be empty. Please try again.")
            continue

        if "://" not in url:
            url = f"https://{url}"

        parsed_url = urlparse(url)
        has_whitespace = any(character.isspace() for character in url)
        if (
            parsed_url.scheme in {"http", "https"}
            and parsed_url.hostname
            and not has_whitespace
        ):
            return url

        print("Please enter a valid web address, such as https://example.com")


def main():
    url = ask_for_url()
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
    file_path = Path(__file__).with_name(f"qrcode_{timestamp}.png")

    qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_M)
    qr.add_data(url)
    qr.make(fit=True)

    image = qr.make_image(fill_color="black", back_color="white")

    try:
        image.save(file_path)
    except OSError as error:
        print(f"Could not save the QR code: {error}")
        raise SystemExit(1)

    print(f"QR code generated for: {url}")
    print(f"Saved at: {file_path}")


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\nCancelled.")
