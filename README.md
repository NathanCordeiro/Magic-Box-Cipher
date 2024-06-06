---
# Magic Box Cipher
---

## Overview
The MagicBox cipher is my own take on the classic keyword substitution cipher.  This type of cipher relies on a secret keyword to create a custom codebook for encryption and decryption. While there are many historical and existing keyword ciphers, the MagicBox cipher offers a unique twist with its approach.

## Why use the magic box cipher?
  - ### `Dynamic Table Creation:`
      - Unlike some keyword ciphers that use pre-defined substitution tables, the MagicBox cipher takes a user-defined keyword and generates a dynamic 5x5 substitution table on the fly. This table serves as the core of the encryption and decryption process. The keyword itself is incorporated into the table, and the remaining slots are filled with the rest of the alphabet. This dynamic table creation adds a layer of variability compared to static ciphers that use pre-determined letter mappings. A static cipher's predictability makes it more susceptible to code-breaking attempts, especially if the underlying table structure is known.

  - <details>

    <summary>  <h2> 👇 NOTE</h2> </summary>

       
       | *While the MagicBox cipher offers a fun and educational way to explore cryptography, it's important to acknowledge its limitations. For truly secure communication, especially when dealing with                sensitive information, stronger encryption algorithms are recommended. However, for specific use cases where a layer of basic obscurity is desired, the MagicBox cipher can be a useful tool.* |
       |:--|
    
    </details>

## License
[![Licence](https://img.shields.io/github/license/Ileriayo/markdown-badges?style=for-the-badge)](./LICENSE)
