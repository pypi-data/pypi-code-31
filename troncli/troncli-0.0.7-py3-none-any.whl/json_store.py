raw_config = {
  " net": {
    " type": "mainnet"
  },

  " storage": {
    " db.version": 1,
    " db.directory": "database",
    " index.directory": "index",
    " index.switch": "off",
    " properties": [
    ]
  },

  " node.discovery": {
    " enable": "true",
    " persist": "true",
    " bind.ip": "",
    " external.ip": "null"
  },

  " node.backup": {
    " port": 10001,
    " priority": 8,
    " members": [
    ]
  },

  " node": {
    " trustNode": "127.0.0.1:50051",
    " walletExtensionApi": "true",
    " listen.port": 18888,
    " connection.timeout": 2,
    " tcpNettyWorkThreadNum": 0,
    " udpNettyWorkThreadNum": 1,
    " connectFactor": 0.3,
    " activeConnectFactor": 0.1,
    " maxActiveNodes": 30,
    " maxActiveNodesWithSameIp": 2,
    " minParticipationRate": 15,
    " disconnectNumberFactor": 0.4,
    " maxConnectNumberFactor": 0.8,
    " receiveTcpMinDataLength": 2048,
    " isOpenFullTcpDisconnect": "true",

    " p2p": {
      " version": 11111
    },

    " active": [
    ],

    " passive": [
    ],

    " http": {
      " fullNodePort": 8090,
      " solidityPort": 8091
    },

    " rpc": {
      " port": 50051,
      " maxConnectionIdleInMillis": 60000
    }
  },

  " seed.node": {
    " ip.list": [
      "54.236.37.243:18888",
      "52.53.189.99:18888",
      "18.196.99.16:18888",
      "34.253.187.192:18888",
      "52.56.56.149:18888",
      "35.180.51.163:18888",
      "54.252.224.209:18888",
      "18.228.15.36:18888",
      "52.15.93.92:18888",
      "34.220.77.106:18888",
      "13.127.47.162:18888",
      "13.124.62.58:18888",
      "13.229.128.108:18888",
      "35.182.37.246:18888",
      "47.90.215.84:18888",
      "47.254.77.146:18888",
      "47.74.242.55:18888",
      "47.75.249.119:18888",
      "47.90.201.118:18888",
      "34.250.140.143:18888",
      "35.176.192.130:18888",
      "52.47.197.188:18888",
      "52.62.210.100:18888",
      "13.231.4.243:18888",
      "47.254.27.69:18888",
      "35.154.90.144:18888",
      "13.125.210.234:18888",
      "47.88.174.175:18888",
      "47.75.249.4:18888"
    ]
  },

  " genesis.block": {
    " assets": [
      {
        " accountName": "Zion",
        " accountType": "AssetIssue",
        " address": "TLLM21wteSPs4hKjbxgmH1L6poyMjeTbHm",
        " balance": "99000000000000000"
      },
      {
        " accountName": "Sun",
        " accountType": "AssetIssue",
        " address": "TXmVpin5vq5gdZsciyyjdZgKRUju4st1wM",
        " balance": "0"
      },
      {
        " accountName": "Blackhole",
        " accountType": "AssetIssue",
        " address": "TLsV52sRDL79HXGGm9yzwKibb6BeruhUzy",
        " balance": "-9223372036854775808"
      }
    ],

    " witnesses": [
      {
        " address": "THKJYuUmMKKARNf7s2VT51g5uPY6KEqnat",
        " url": "http://GR1.com",
        " voteCount": 100000026
      },
      {
        " address": "TVDmPWGYxgi5DNeW8hXrzrhY8Y6zgxPNg4",
        " url": "http://GR2.com",
        " voteCount": 100000025
      },
      {
        " address": "TWKZN1JJPFydd5rMgMCV5aZTSiwmoksSZv",
        " url": "http://GR3.com",
        " voteCount": 100000024
      },
      {
        " address": "TDarXEG2rAD57oa7JTK785Yb2Et32UzY32",
        " url": "http://GR4.com",
        " voteCount": 100000023
      },
      {
        " address": "TAmFfS4Tmm8yKeoqZN8x51ASwdQBdnVizt",
        " url": "http://GR5.com",
        " voteCount": 100000022
      },
      {
        " address": "TK6V5Pw2UWQWpySnZyCDZaAvu1y48oRgXN",
        " url": "http://GR6.com",
        " voteCount": 100000021
      },
      {
        " address": "TGqFJPFiEqdZx52ZR4QcKHz4Zr3QXA24VL",
        " url": "http://GR7.com",
        " voteCount": 100000020
      },
      {
        " address": "TC1ZCj9Ne3j5v3TLx5ZCDLD55MU9g3XqQW",
        " url": "http://GR8.com",
        " voteCount": 100000019
      },
      {
        " address": "TWm3id3mrQ42guf7c4oVpYExyTYnEGy3JL",
        " url": "http://GR9.com",
        " voteCount": 100000018
      },
      {
        " address": "TCvwc3FV3ssq2rD82rMmjhT4PVXYTsFcKV",
        " url": "http://GR10.com",
        " voteCount": 100000017
      },
      {
        " address": "TFuC2Qge4GxA2U9abKxk1pw3YZvGM5XRir",
        " url": "http://GR11.com",
        " voteCount": 100000016
      },
      {
        " address": "TNGoca1VHC6Y5Jd2B1VFpFEhizVk92Rz85",
        " url": "http://GR12.com",
        " voteCount": 100000015
      },
      {
        " address": "TLCjmH6SqGK8twZ9XrBDWpBbfyvEXihhNS",
        " url": "http://GR13.com",
        " voteCount": 100000014
      },
      {
        " address": "TEEzguTtCihbRPfjf1CvW8Euxz1kKuvtR9",
        " url": "http://GR14.com",
        " voteCount": 100000013
      },
      {
        " address": "TZHvwiw9cehbMxrtTbmAexm9oPo4eFFvLS",
        " url": "http://GR15.com",
        " voteCount": 100000012
      },
      {
        " address": "TGK6iAKgBmHeQyp5hn3imB71EDnFPkXiPR",
        " url": "http://GR16.com",
        " voteCount": 100000011
      },
      {
        " address": "TLaqfGrxZ3dykAFps7M2B4gETTX1yixPgN",
        " url": "http://GR17.com",
        " voteCount": 100000010
      },
      {
        " address": "TX3ZceVew6yLC5hWTXnjrUFtiFfUDGKGty",
        " url": "http://GR18.com",
        " voteCount": 100000009
      },
      {
        " address": "TYednHaV9zXpnPchSywVpnseQxY9Pxw4do",
        " url": "http://GR19.com",
        " voteCount": 100000008
      },
      {
        " address": "TCf5cqLffPccEY7hcsabiFnMfdipfyryvr",
        " url": "http://GR20.com",
        " voteCount": 100000007
      },
      {
        " address": "TAa14iLEKPAetX49mzaxZmH6saRxcX7dT5",
        " url": "http://GR21.com",
        " voteCount": 100000006
      },
      {
        " address": "TBYsHxDmFaRmfCF3jZNmgeJE8sDnTNKHbz",
        " url": "http://GR22.com",
        " voteCount": 100000005
      },
      {
        " address": "TEVAq8dmSQyTYK7uP1ZnZpa6MBVR83GsV6",
        " url": "http://GR23.com",
        " voteCount": 100000004
      },
      {
        " address": "TRKJzrZxN34YyB8aBqqPDt7g4fv6sieemz",
        " url": "http://GR24.com",
        " voteCount": 100000003
      },
      {
        " address": "TRMP6SKeFUt5NtMLzJv8kdpYuHRnEGjGfe",
        " url": "http://GR25.com",
        " voteCount": 100000002
      },
      {
        " address": "TDbNE1VajxjpgM5p7FyGNDASt3UVoFbiD3",
        " url": "http://GR26.com",
        " voteCount": 100000001
      },
      {
        " address": "TLTDZBcPoJ8tZ6TTEeEqEvwYFk2wgotSfD",
        " url": "http://GR27.com",
        " voteCount": 100000000
      }
    ],

    " timestamp": "0",

    " parentHash": "0xe58f33f9baf9305dc6f82b9f1934ea8f0ade2defb951258d50167028c780351f"
  },

  " localwitness": [
  ],

  " block": {
    " needSyncCheck": "true",
    " maintenanceTimeInterval": 21600000,
    " proposalExpireTime": 259200000
  },


  " vm": {
    " supportConstant": "false",
    " minTimeRatio": 0.0,
    " maxTimeRatio": 5.0
  },

  " committee": {
    " allowCreationOfContracts": 0
  },

  " log.level": {
     " root": "INFO"
  }
}