---
layout: post
title: "Import transactions from MoneyWiz to Ledger"
date: 2017-06-20 14:42
---

I've been using MoneyWiz for years and I really love it for its good balance between usability and functionality. However, its synchronization replies on its commercial cloud service which makes me a little bit afraid. I have to regularly backup my transactions via its "Export to csv" option. On the other hand, Ledger has drawn my attention for a quite long time as I really appreciate its idea of plain text accounting. Also, double entry accounting sounds more universal and professional. Surely, its complexity makes it impractical for daily usage without an mature mobile app. Therefore, I decide to backup my transactions in ledger format and keep using MoneyWiz for daily usage.

First, a demo of my exported csv file from MoneyWiz (`moneywiz.csv`) is shown below below:

```
sep=,
"Name","Current balance","Account","Transfers","Description","Payee","Category","Date","Memo","Amount","Currency","Check #","Tags","Balance"
"Cash","2,307.07","","","","","","","","","","","",""
"","","Cash","","Opening balance","","Other","09/26/2012","","1,839.42","CNY","","","+1,839.42"
"","","Cash","","Lunch","","Food > Dining","09/27/2012","","-9.33","CNY","","","+1,830.09"
"","","Cash","","Snacks","","Food > Dining","09/27/2012","","-2.28","CNY","","","+1,827.81"
"","","Cash","","Dining","","Shopping > Books","09/27/2012","","-20.74","CNY","","","+1,807.07"
"","","Cash","ICBC","ATM Withdrawal","","","09/30/2015","","500.00","CNY","","","+2,307.07"
"ICBC","8,506.37","","","","","","","","","","","",""
"","","ICBC","","Opening balance","","Other","09/28/2012","","7,277.11","CNY","","","+7,277.11"
"","","ICBC","","Other","","Other","09/28/2015","Grants","29.26","CNY","","","+7,306.37"
"","","ICBC","","Salary & Wages","","Salary","09/29/2015","","1,700.00","CNY","","","+9,006.37"
"","","ICBC","Cash","ATM Withdrawal","","","09/30/2015","","-500.00","CNY","","","8,506.37"
```

We need to pre-process this file now and there are two things to notice. Firstly, all the fields are quoted by double quotes and there are commas in some fields which should not be regarded as separators. This is implemented by **FPAT** variable which is only supported by gawk version 4+. Secondly, transactions in this file are organized based on Accounts. Transactions of transfer/withdraw are different from normal income/expenses. One single transfer event corresponds to two records: one for transfer-from and one for transfer-to. Here is the awk file named by `moneywiz.awk` I use for pre-process and run as `./moneywiz.awk moneywiz.csv > moneywiz-tmp.csv`.

``` awk
#!/usr/bin/env gawk -f

BEGIN {
    # ignore commas in quotes
    # FS = ","
    FPAT = "[^,]*|\"[^\"]*\""
    print("\"account\",\"date\",\"amount\",\"currency\",\"category\",\"payee\",\"description\",\"memo\",\"balance\",\"type\"")
}
NR > 2 {
    name = $1
    current_balance = $2
    account = $3
    transfers = $4
    description = $5
    payee = $6
    gsub(" > ", ":", $7)
    category = $7
    date = $8
    memo = $9
    amount = $10
    currency = $11
    check = $12
    tags = $13
    balance = $14
    if (account == "\"\"" || account == "") {
        next
    }
    if (match(amount, "-")) {
        type = "\"Expenses\""
    } else {
        type = "\"Income\""
    }
    if (transfers != "\"\"" && transfers != "") {
        type = "\"Transfers\""
        payee = transfers
        # skip duplicating transactions of transfers
        am = amount
        gsub("-", "", am)
        gsub("+", "", am)
        if (seen[account"-"transfers"-"date"-"am]++ || seen[transfers"-"account"-"date"-"am]++) {
            next
        }
    }
    printf("%s,%s,%s,%s,%s,%s,%s,%s,%s,%s\n", account, date, amount, currency, category, payee, description, memo, balance, type)
}
```

The content of file `moneywiz-tmp.csv` is like:

```
"account","date","amount","currency","category","payee","description","memo","balance","type"
"Cash","09/26/2012","1,839.42","CNY","Other","","Opening balance","","+1,839.42","Income"
"Cash","09/27/2012","-9.33","CNY","Food:Dining","","Lunch","","+1,830.09","Expenses"
"Cash","09/27/2012","-2.28","CNY","Food:Dining","","Snacks","","+1,827.81","Expenses"
"Cash","09/27/2012","-20.74","CNY","Shopping:Books","","Dining","","+1,807.07","Expenses"
"Cash","09/30/2015","500.00","CNY","","ICBC","ATM Withdrawal","","+2,307.07","Transfers"
"ICBC","09/28/2012","7,277.11","CNY","Other","","Opening balance","","+7,277.11","Income"
"ICBC","09/28/2015","29.26","CNY","Other","","Other","Grants","+7,306.37","Income"
"ICBC","09/29/2015","1,700.00","CNY","Salary","","Salary & Wages","","+9,006.37","Income"
```

Now, we can convert this pre-processed csv file to ledger format accordign to rules. Related information can be found in [here](https://github.com/simonmichael/hledger/tree/master/examples/csv). The `moneywiz-tmp.csv.rules` is like:

```
# hledger CSV conversion rules for MoneyWiz's register export format

skip 1

fields account, date, amount, currency-del, category, payee, description, memo, balance, type

date-format %m/%d/%Y
amount %amount CNY
description %description
account1 Assets:%account
if Expenses
   account2 Expenses:%category
   comment %payee
if Income
   account2 Income:%category
   comment %payee
if Transfers
   account2 Assets:%payee
status *
```

Now, just run: `hledger -f moneywiz-tmp.csv print > moneywiz.ledger`. The output file `moneywiz.ledger` is like:

```
2012/09/26 * Opening balance
    Income:Other                           -1,839.42 CNY
    Assets:Cash                             1,839.42 CNY

2012/09/27 * Lunch
    Expenses:Food:Dining                        9.33 CNY
    Assets:Cash                                -9.33 CNY

2012/09/27 * Snacks
    Expenses:Food:Dining                        2.28 CNY
    Assets:Cash                                -2.28 CNY

2012/09/27 * Dining
    Expenses:Shopping:Books                    20.74 CNY
    Assets:Cash                               -20.74 CNY

2012/09/28 * Opening balance
    Income:Other                           -7,277.11 CNY
    Assets:ICBC                             7,277.11 CNY

2015/09/28 * Other
    Income:Other                              -29.26 CNY
    Assets:ICBC                                29.26 CNY

2015/09/29 * Salary & Wages
    Income:Salary                          -1,700.00 CNY
    Assets:ICBC                             1,700.00 CNY

2015/09/30 * ATM Withdrawal
    Assets:ICBC                              -500.00 CNY
    Assets:Cash                               500.00 CNY
```
