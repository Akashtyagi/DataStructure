#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 23:42:35 2020

@author: AkashTyagi
"""

from collections import Counter
from queue import PriorityQueue

class HauffmanNode:
    def __init__(self, char, frequency=0, left=None, right=None):
        self.char = char
        self.frequency = frequency
        self.left = left
        self.right = right
        
    def __lt__(self, other):
        return self.frequency < other.frequency


def _create_encoding(node, code, encoding_table):
    if node.char is not None:
        encoding_table[node.char] = code
    else:
        _create_encoding(node.left, code+'0', encoding_table)
        _create_encoding(node.right, code+'1', encoding_table)


def _create_tree_encoding(node, tree_encoding):
    '''
    Creates encoding of the Haufmann tree obtained.
    '''
    if node.char is not None:
        tree_encoding += "1"
        tree_encoding += f"{ord(node.char):08b}"
    else:
        tree_encoding += "0"
        tree_encoding = _create_tree_encoding(node.left, tree_encoding)
        tree_encoding = _create_tree_encoding(node.right, tree_encoding)
    return tree_encoding
        

# =============================================================================
# Encoding the Input
# =============================================================================
def encode_text(text):
    word_frequencies = Counter(text)
    queue = PriorityQueue() # Queue Initialisation
    
    # Creating Hauffman Tree
    for word,freq in word_frequencies.items(): # Creates a priority queue
        queue.put(HauffmanNode(char=word, frequency=freq))
        
    encoding_table = {}
    
    # Create queue with Empty Parent node & frequency=sum of child
    while queue.qsize()>1:
        left_node, right_node = queue.get(), queue.get()
        # Place a empty node above chars
        queue.put(HauffmanNode(char=None, 
                               frequency= (left_node.frequency + right_node.frequency),
                               left= left_node, 
                               right= right_node 
                               ))
    
    hauffmanHead = queue.get() # Instance of Hauffman tree
    
    _create_encoding(hauffmanHead, '', encoding_table)
    
    
    # Input text encoding
    encoded_text_code = ''
    for s in text:
        encoded_text_code += encoding_table[s]
    
    # Encoding of Hauffman tree    
    tree_encoding = ''
    tree_encoding = _create_tree_encoding(hauffmanHead, tree_encoding)
           
    '''
    Suppose the scenario:
        Text-Encoding = 1000001 
        len(Text-Encoding) = 7
        
        127 is not a perfect 8bit code, so :
            7%8 = 7
            8-7 = 1 <-Q
                Therefore, we are lacking 1 bit to make it perfect 8bit code.
        
        So we add 0*Q number of 0's to the code:
            Text-Encoding : 01000001  <- This is perfect 8bit code
        
        And then Q is also stored to keep track how many zero numbers were added.
        so ord(1) - 00000001
        Final encoding: TreeEncoding + QEncoding + TextEncoding  
    '''
    bit_size_of_encoding = len(encoded_text_code) + len(tree_encoding)
    bits_less_for_8bit_code = 8 - bit_size_of_encoding%8
    if bits_less_for_8bit_code != 0: 
        # Extra bits needed to be added to make file of 8 bit pattern
        encoded_text_code = "0"*bits_less_for_8bit_code + encoded_text_code
        
    ''' 
    Final encoding is of form
    -------------------------
            Tree Encoding->Extra 0 binary added->Input Encoding. 
    '''    
    final_encoding = f"{tree_encoding}{bits_less_for_8bit_code:08b}{encoded_text_code}"
    return final_encoding
 
# =============================================================================
# Decoding the encoding
# =============================================================================


def _decode_hauffman_tree(encoding_array):
    '''
    Extracts Hauffman tree from input encoding.
    
    Approach:
    --------
    As encoded in the encoding tree, the node containing actual input words
    are encoded with 1 and all remaining are encoded with 0.
    So we need to to recursively iterate untill we find 1.
    '''
    encoded_bit = encoding_array[0]
    del encoding_array[0] # we delete it so in future we do not refer to same bit.
    
    if encoded_bit == "1":
        ''' 
        It means the next bit is a char, and as we have converted every char
        into its 8bit equivalent representation of its ASCII value, we will
        iterate to find out next 8 bits and then convert it into a char.
        '''
        char = "" # Initially contain 8bit equivalent encoding
        for _ in range(8):
           char += encoding_array[0]
           del encoding_array[0]
        return HauffmanNode(chr(int(char, 2)))
    return HauffmanNode(None, left= _decode_hauffman_tree(encoding_array), \
                        right= _decode_hauffman_tree(encoding_array))

def decode_encoding(final_encoding):
    # First we extract the Tree Encoding
    encoding_array = list(final_encoding) # Encoding is converted into array for easy index access
    decoded_hauffman_tree = _decode_hauffman_tree(encoding_array)
    
    
    
    # Removing extra binarry added for file balancing
    '''
    Suppose the scenario:
        Text-Encoding = 1000001 
        len(Text-Encoding) = 7
        
        127 is not a perfect 8bit code, so :
            7%8 = 7
            8-7 = 1 <-Q
                Therefore, we are lacking 1 bit to make it perfect 8bit code.
        
        So we add 0*Q number of 0's to the code:
            Text-Encoding : 0-1000001  <- This is perfect 8bit code
        
        And then Q is also stored to keep track how many zero numbers were added.
        so ord(1) - 00000001
        Final encoding: TreeEncoding + QEncoding + TextEncoding     
    '''
        
    # Here first we remove the QEncoding, which is always 8-bits
    extra_0_binaries = encoding_array[:8] 
    encoding_array = encoding_array[8:] # The actual text-encoding is after 8 bits.
    number_of_0_added = int("".join(extra_0_binaries),2) 
    # Now we remove the actuall number of extra zero added.
    encoding_array = encoding_array[number_of_0_added:] 
    
    
    '''
    Now we iterate through encoded_text and follow below instructions:
        
        If encoded-bit == 0:
            Go to left of hauffman tree
                If left-child of Current root is not None, means we have reached leaf,
                    Extract Value, set root to initial Hauffman tree again.
        
        If encoded-bit == 1:
            Go to right of hauffman tree
                If right-child of Current root is not None, means we have reached leaf,
                    Extract Value, set root to initial Hauffman tree again.
    '''
    decoded_text = ''
    current_node = decoded_hauffman_tree
    for char in encoding_array:
        if char=='0' :
            current_node = current_node.left
        else:
            current_node = current_node.right
        
        if current_node.char is not None:
            decoded_text += current_node.char
            current_node = decoded_hauffman_tree
            
    return decoded_text

if __name__ == "__main__":
    text = "this is demo text called in  the call=for !!"
    print("Input Text: ",text)
    encoding = encode_text(text)
    print("Encoding: ",encoding)
    decoded_text = decode_encoding(encoding)
    print("Decoded Text: ",decoded_text)
