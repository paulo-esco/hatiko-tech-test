class ImeiValidator:
    @staticmethod
    def is_valid(imei: str) -> bool:
        imei = imei.strip().replace(" ", "").replace("-", "")
        if not imei.isdigit() or len(imei) != 15:
            return False

        total = 0
        reverse_digits = imei[::-1]
        for i, d in enumerate(reverse_digits):
            n = int(d)
            if i % 2 == 1:
                n *= 2
                if n > 9:
                    n -= 9
            total += n
        return total % 10 == 0
