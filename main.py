from logic import KeppnirLogic, LengdKeppnaLogic

if __name__ == "__main__":
    keppnir = KeppnirLogic()
    lengd_keppna = LengdKeppnaLogic()

    keppnir.save_keppnir()
    lengd_keppna.save_lengd_keppna()