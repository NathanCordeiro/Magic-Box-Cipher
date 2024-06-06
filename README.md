---
# Magic Box Cipher
---

## Overview
The MagicBox cipher is my own take on the classic keyword substitution cipher.  This type of cipher relies on a secret keyword to create a custom codebook for encryption and decryption. While there are many historical and existing keyword ciphers, the MagicBox cipher offers a unique twist with its approach.

## Why use the magic box cipher?
  - ### `Dynamic Table Creation:`
      - Unlike some keyword ciphers that use pre-defined substitution tables, the MagicBox cipher takes a user-defined keyword and generates a dynamic 5x5 substitution table on the fly. This table serves as the core of the encryption and decryption process. The keyword itself is incorporated into the table, and the remaining slots are filled with the rest of the alphabet. This dynamic table creation adds a layer of variability compared to static ciphers that use pre-determined letter mappings. A static cipher's predictability makes it more susceptible to code-breaking attempts, especially if the underlying table structure is known.

## License
[![Licence](https://img.shields.io/github/license/Ileriayo/markdown-badges?style=for-the-badge)](./LICENSE)
