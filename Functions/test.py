from LnmFunctions import Trading as tr


trader = tr(
    key="tJlOA0pSR8PRTZksov3iqGhRbqaYktS4F5tbYK+dDQ8=",
    secret="I6d2pLEZln+yGHPXZzlGvN5XFCxsnDRQnllikA4JNTADPNct/3zMr7nLFJ593YUzCuKAsqfKZCXWGAkJrHdQ9w==",
    passphrase="9d0hb89h1e4e6")


print(trader.long(margin=200, leverage=40, type="l", entry_price=19500))
