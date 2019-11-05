---
layout: post
title: "Notes on GPG"
date: 2017-07-02 13:27
---

Security really matters these
years[^1]. [WannaCry](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=4&cad=rja&uact=8&ved=0ahUKEwiJmZDu8-nUAhUCX5QKHURUDmIQFgg5MAM&url=https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FWannaCry_ransomware_attack&usg=AFQjCNF1ODznJ6dREATHzLd24K2eiV173A) gave
us a global warning early this year. Before, Chinese netizens feel
quite safe maybe because of few technology audience... or rather GFW
helps? With the technology's deeper root in life accompanied by mobile
payment, online shopping, smart stuff and the like, I believe security
issue is critical enough to draw everyone's attention. Security is the
most inevitable thing even if one may ignore privacy problem for now.

Okay, here is my notes
on [GPG](https://en.wikipedia.org/wiki/GNU_Privacy_Guard). I only
introduce my commonly used options and all the details are
in [GnuPG manual](https://www.gnupg.org/documentation/manuals/gnupg/).

## Options

- `-k/--list-public-keys`: List public keys.
- `-K/--list-secret-keys`: List private keys.
- `-e/--encrypt`: Encrypt data by specifying public key (recipient).
- `-s/--sign`: Sign a message by key.
- `-c/--symmetric`: Encrypt with a symmetric cipher using a passphrase.
- `--cipher-algo`: Specify cipher algorithm. (list all available by running `gpg --version`)
- `-d/--decrypt`: Decrypt data.
- `-r/--recipient`: This option is used for specifying the recipient (user-id).
- `-a/--armor`: Create ASCII output.
- `-o/--output`: Specify output file name.
- `--clear-sign`: Add signature to the original file.
- `--detach-sign`: Generate a signature separately.

## Examples

### Basic Encryption
```sh
gpg -r chris -e foo.txt
# It creates foo.txt.gpg
```

### Encrypt with Symmetric Cipher
```sh
gpg -c foo.txt
# Enter passphase twice and foo.txt.gpg is created.
```

### ASCII output
```sh
gpg -c -a foo.txt
# Enter passphase twice and foo.txt.asc is created.
```

### Using with pipeline
```sh
echo "hello" | gpg -c -a -
# -----BEGIN PGP MESSAGE-----
#
# jA0EBwMCI9EOCv8RfTDh0jsB6f1PHXr7CnPvtFQ3+1xzVkaaFT0NGnaXV7vp0TA6
# yQaOCS806a4Gg7/3UxBcPqm1t74asvk2tgm06Q==
# =fstr
# -----END PGP MESSAGE-----
```

### Sign and verify
```sh
gpg --clear-sign foo.txt
# File foo.txt.asc which is not encrypted is generated
gpg -d foo.txt.asc # show raw data and verify signature
gpg --verify foo.txt.asc # verify signature
```

### Detached sign
```sh
gpg --detach-sign foo.txt
# File foo.txt.sig (notice its size) is generated
gpg --verify foo.txt.sig foo.txt # verify signature
```

### Output to stdout
```sh
gpg -o - -ac foo.txt
# -----BEGIN PGP SIGNATURE-----
# 
# iQEzBAABCAAdFiEEiul6fOyv8uDC/NJyNkEjOM7Lx3AFAllZ9bYACgkQNkEjOM7L
# x3DWtggAg+ACLCf4uDutKZNen9JQEMsoxlNmCoZpfTraE5Hy6eeZ3m4CV8YlpPup
# Qhl9ajFvvTL8pdS3e6LSWvViZ3MRfTYi8bxfpb4Erv4Isk+kCIZJwG7QmFCKLtCA
# ERoj1Mygt2AL7mPQBWKWtetYGrbScOPRNKu/cRhazbovHoUJbgtjZRpyn9+U9lRz
# OEBJTBqFO4p4uefbwstMLg+ZnId3Q2MTqmb0DGuu4GRUpDQf2U+R+6meTprjayPE
# T1QDHpI9hQ9gto0PGT3G9hSAWIJqxLXytltTAclPNVv62GhBEfgh10zRe1wkhYiz
# uXM+IG4guxTRIAynlz6esmyGHoer/g==
# =qDbQ
# -----END PGP SIGNATURE-----
```

---

[^1]: [收到的邮件内容被篡改了](https://www.v2ex.com/t/372427)
