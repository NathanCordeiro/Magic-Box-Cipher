---
# Magic Box Cipher
---

## Overview
**The MagicBox cipher is my own take on the classic keyword substitution cipher.  This type of cipher relies on a secret keyword to create a custom codebook for encryption and decryption. While there are many historical and existing keyword ciphers, the MagicBox cipher offers a unique twist with its approach.**

## Why use the magic box cipher?
  - ### `Dynamic Table Creation:`
      - Unlike some keyword ciphers that use pre-defined substitution tables, the MagicBox cipher takes a user-defined keyword and generates a dynamic 5x5 substitution table on the fly. This table serves as the core of the encryption and decryption process. The keyword itself is incorporated into the table, and the remaining slots are filled with the rest of the alphabet. This dynamic table creation adds a layer of variability compared to static ciphers that use pre-determined letter mappings. A static cipher's predictability makes it more susceptible to code-breaking attempts, especially if the underlying table structure is known.

  - ### `Customizable Transposition Key:`
      - The Magic Box Cipher offers an additional layer of security through the use of a customizable transposition key. This key is a sequence of numbers used to rearrange the rows or columns of the encrypted message, adding complexity beyond the initial substitution step. By allowing users to choose their own transposition key or use a default one, the cipher provides a flexible yet powerful method to further obfuscate the message. This feature is particularly useful because even if an attacker understands the substitution grid, they still need to decipher the additional transposition step to fully decode the message.

  - <details>

    <summary>  <h2> 👇 NOTE</h2> </summary>

       
       | *While the MagicBox cipher offers a fun and educational way to explore cryptography, it's important to acknowledge its limitations. For truly secure communication, especially when dealing with                sensitive information, stronger encryption algorithms are recommended. However, for specific use cases where a layer of basic obscurity is desired, the MagicBox cipher can be a useful tool.* |
       |:--|

    ---
    </details>

## Code Explanation

## Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/NathanCordeiro/Magic-Box-Cipher.git
   ```
2. Navigate to the project directory:
   ```sh
   cd Magic-Box-Cipher
   ```
## Usage
1. Run the script:
   ```sh
   python cipher.py
   ```
2. Choose whether to encrypt (E) or decrypt (D) a message.
3. Enter the message and keyword as prompted.

## License
[![Licence](https://img.shields.io/github/license/Ileriayo/markdown-badges?style=for-the-badge)](./LICENSE)
