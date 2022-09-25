from .base import PgObject


class Bitmapset(PgObject):
    bits_per_word = 64

    def to_string(self):
        nwords = self.val["nwords"]

        exps = list()
        for i in range(nwords):
            num = self.val["words"][i]
            for b in range(self.bits_per_word):
                if num % 2 == 1:
                    exps.append(str(b + i * self.bits_per_word))

                num = num >> 1

        return "<Bitmapset {}>".format(" ".join(exps))
