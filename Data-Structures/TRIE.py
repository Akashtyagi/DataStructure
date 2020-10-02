#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 02:12:24 2020

@author: AkashTyagi
"""

# =============================================================================
# TRIE
# =============================================================================
class TrieNode:
    '''
    Initialize base Data-Structure of Trie
    '''
    def __init__(self,char="/"):
        self.char = char # Character value at specific level
        self.characters= {} # Character dict containing following characters.
        self.word_end = 0 # 0 no. of words ends at this point.
    
    
class Trie:
    def __init__(self):
        self.root = TrieNode() # root points to a TrieNode [char,characters,word_end]
        
        
    def insert(self,word):
        ''' Insert string into Trie '''
        head = self.root 
        
        for char in word:
            if char not in head.characters: # New Character
                head.characters[char] = TrieNode(char) # Intialize new TrieNode inside present char character-set.
            head = head.characters[char] # Move to next character
        head.word_end+=1    # Represent word ended at this character.


    def search(self,word):
        ''' Search string in Trie '''
        head = self.root
        
        for char in word:
            if char not in head.characters: # Char not present in head characters, No such word exist.
                return False
            head = head.characters[char] # Move to next character
        return head.word_end>0 # Check that last character represent end of word.
    
    
    def startswith(self,word):
        ''' Find prefix of actual string. '''
        head = self.root
        
        for char in word:
            if char not in head.characters: # Char not present in head characters, No such word exist.
                return False
            head = head.characters[char] # Move to next character
        return head.word_end==0 # Verify that it is not end of string.
    
dc = Trie()
dc.insert("akash")
dc.insert("amit")
dc.insert("anmol")
dc.insert("bad")

print(dc.search("bad"))

print(dc.startswith("aka"))
    
            
            
            