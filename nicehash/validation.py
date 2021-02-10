def validate_dict(items: dict):
    for k, v in items.items():
        if v:
            accepted = accepted_values(key=k)
            if accepted:
                validate(key=k, value=v, accepted=accepted)


def accepted_values(key):
    if key == "sortDirection":
        return ['ASC', 'DESC']
    elif key == "orderState":
        return ["CREATED", "RESERVED", "RESERVATION_ERROR", "INSERTED", "INSERTED_ERROR", "RELEASED",
                "RELEASED_ERROR", "PARTIAL", "ENTERED", "FULL", "PROCESSED_ERROR", "CANCEL_REQUEST", "CANCELLED",
                "CANCELLED_ERROR", "REJECTED"]
    elif key == "orderStatus":
        return ["all", "completed", "open", "executed"]
    elif key == "side":
        return ["BUY", "SELL"]
    elif key == "type":
        return ["LIMIT", "MARKET", "STANDARD",
                "FIXED"]  # blending two validation rules together because they share the same key.
        # Hopefully this proves to be an edge case
    elif key == "algorithm":
        return ["SCRYPT", "SHA256", "SCRYPTNF", "X11", "X13", "KECCAK", "X15", "NIST5", "NEOSCRYPT", "LYRA2RE",
                "WHIRLPOOLX", "QUBIT", "QUARK", "AXIOM", "LYRA2REV2", "SCRYPTJANENF16", "BLAKE256R8", "BLAKE256R14",
                "BLAKE256R8VNL", "HODL", "DAGGERHASHIMOTO", "DECRED", "CRYPTONIGHT", "LBRY", "EQUIHASH", "PASCAL",
                "X11GOST", "SIA", "BLAKE2S", "SKUNK", "CRYPTONIGHTV7", "CRYPTONIGHTHEAVY", "LYRA2Z", "X16R",
                "CRYPTONIGHTV8", "SHA256ASICBOOST", "ZHASH", "BEAM", "GRINCUCKAROO29", "GRINCUCKATOO31", "LYRA2REV3",
                "CRYPTONIGHTR", "CUCKOOCYCLE", "GRINCUCKAROOD29", "BEAMV2", "X16RV2", "RANDOMXMONERO", "EAGLESONG",
                "CUCKAROOM", "GRINCUCKATOO32", "HANDSHAKE", "KAWPOW", "CUCKAROO29BFC", "BEAMV3", "CUCKAROOZ29",
                "OCTOPUS"]
    elif key == "status":
        return ["VERIFIED", "NOT_VERIFIED"]
    elif key == "poolVerificationServiceLocation":
        return ["EUROPE", "USA"]
    elif key == "market":
        return ["EU", "USA"]
    elif key == "miningAlgorithm":
        return ["SCRYPT", "SHA256", "SCRYPTNF", "X11", "X13", "KECCAK", "X15", "NIST5", "NEOSCRYPT", "LYRA2RE",
                "WHIRLPOOLX", "QUBIT", "QUARK", "AXIOM", "LYRA2REV2", "SCRYPTJANENF16", "BLAKE256R8", "BLAKE256R14",
                "BLAKE256R8VNL", "HODL", "DAGGERHASHIMOTO", "DECRED", "CRYPTONIGHT", "LBRY", "EQUIHASH", "PASCAL",
                "X11GOST", "SIA", "BLAKE2S", "SKUNK", "CRYPTONIGHTV7", "CRYPTONIGHTHEAVY", "LYRA2Z", "X16R",
                "CRYPTONIGHTV8", "SHA256ASICBOOST", "ZHASH", "BEAM", "GRINCUCKAROO29", "GRINCUCKATOO31", "LYRA2REV3",
                "CRYPTONIGHTR", "CUCKOOCYCLE", "GRINCUCKAROOD29", "BEAMV2", "X16RV2", "RANDOMXMONERO", "EAGLESONG",
                "CUCKAROOM", "GRINCUCKATOO32", "HANDSHAKE", "KAWPOW", "CUCKAROO29BFC", "BEAMV3", "CUCKAROOZ29",
                "OCTOPUS"]
    elif key == "sortParameter":
        return ["RIG_NAME", "TIME", "MARKET", "ALGORITHM", "UNPAID_AMOUNT", "DIFFICULTY", "SPEED_ACCEPTED",
                "SPEED_REJECTED", "PROFITABILITY"]
    elif key == "action":
        return ["START", "STOP", "POWER_MODE"]
    elif key == "sort":
        return ["NAME", "PROFITABILITY", "ACTIVE", "INACTIVE"]
    elif key == "op":
        return ["GT", "GE", "LT", "LE"]
    elif key == "stage":
        return ["COMPLETED", "OPEN", "ALL"]
    elif key == "walletType":
        return ["BITGO", "BLOCKCHAIN", "LIGHTNING", "MULTISIG"]
    elif key == "currency":
        return ["BTC", "ETH", "XRP", "BCH", "LTC", "ZEC", "DASH", "XLM", "EOS", "USDT", "BSV", "LINK", "BAT", "PAX",
                "ZRX", "HOT", "OMG", "REP", "NEXO", "BTG", "EURKM", "ENJ", "MATIC", "ELF", "SNT", "BNT", "KNC", "MTL",
                "POLY", "POWR", "GTO", "LOOM", "CVC", "AST", "PPT", "LRC", "KEY", "STORJ", "STORM", "TNT", "DATA",
                "AOA", "RDN", "USDC", "FET", "ANT", "AERGO", "LBA", "XMR", "MITH", "BAND", "SXP", "EURS", "WBTC", "RVN",
                "TBTC", "TETH", "TXRP", "TBCH", "TLTC", "TZEC", "TDASH", "TXLM", "TEOS", "TERC", "TBSV", "TBTG",
                "TEURKM", "TXMR", "TRVN"]
    else:
        return []


def validate(key, value, accepted):
    if value not in accepted:
        raise Exception(f"Valid {key} options: {', '.join(accepted)}")
