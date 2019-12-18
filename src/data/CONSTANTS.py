# PGCA

clipname_templete = "A007_P082_G002_C001"
AIR_P_slc = clipname_templete.find("P")
AIR_P_slc = slice(AIR_P_slc + 1, AIR_P_slc + 4)
AIR_A_slc = clipname_templete.find("A")
AIR_A_slc = slice(AIR_A_slc + 1, AIR_A_slc + 4)
AIR_G_slc = clipname_templete.find("G")
AIR_G_slc = slice(AIR_G_slc + 1, AIR_G_slc + 4)
AIR_C_slc = clipname_templete.find("c")
AIR_C_slc = slice(AIR_C_slc + 1, AIR_C_slc + 4)

CLIPNAME_CONVERTER_PGCA = lambda clipath: (clipath.stem[AIR_P_slc],
                                           clipath.stem[AIR_G_slc],
                                           clipath.stem[AIR_C_slc],
                                           clipath.stem[AIR_A_slc])

TRAIN = "train"
TEST = "test"
VALID = "valid"

tmp_test_clipnames = {
  "A001_P003_G001_C001",  "A001_P003_G001_C002",  "A001_P003_G001_C003",  "A001_P003_G001_C004",
  "A001_P003_G001_C005",  "A001_P003_G001_C006",  "A001_P003_G001_C007",  "A001_P003_G001_C008",
  "A001_P003_G002_C001",  "A001_P003_G002_C002",  "A001_P003_G002_C003",  "A001_P003_G002_C004",
  "A001_P003_G002_C005",  "A001_P003_G002_C006",  "A001_P003_G002_C007",  "A001_P003_G002_C008",
  "A001_P003_G003_C001",  "A001_P003_G003_C002",  "A001_P003_G003_C003",  "A001_P003_G003_C004",
  "A001_P003_G003_C005",  "A001_P003_G003_C006",  "A001_P003_G003_C007",  "A001_P003_G003_C008",
  "A001_P003_G004_C001",  "A001_P003_G004_C002",  "A001_P003_G004_C003",  "A001_P003_G004_C004",
  "A001_P003_G004_C005",  "A001_P003_G004_C006",  "A001_P003_G004_C007",  "A001_P003_G004_C008",
}

AIR_CS_TRAIN_VALIDATOR = lambda filename: int(filename[AIR_P_slc]) % 3 != 0
AIR_CS_VALID_VALIDATOR = lambda filename: int(filename[AIR_P_slc]) % 3 == 0
# AIR_CS_VALID_VALIDATOR = lambda filename: filename in tmp_test_clipnames
AIR_CS_VALIDATOR_DICT = {
  TRAIN: AIR_CS_TRAIN_VALIDATOR,
  TEST: AIR_CS_VALID_VALIDATOR,
  VALID: AIR_CS_VALID_VALIDATOR
}