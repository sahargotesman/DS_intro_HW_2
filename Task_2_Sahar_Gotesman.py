#!/usr/bin/env python3
# -*- coding: utf-8 -*-


#Sahar Gotesman 206014300
###Task 2

#Q1

def reverse(sentence,reverse_word):
    if not isinstance(sentence, str) or not isinstance(reverse_word, str):
        return "invalid input"
    if reverse_word not in sentence:
        return "The word was not found"
    i = sentence.find(reverse_word)
    k=i+len(reverse_word)
    reverse_sentence = sentence[:i] + reverse_word[::-1] + sentence[k::]
    return reverse_sentence
 

# print(reverse("I like apples and I also like bananas", "like")) #should return: "I ekil apples and I also like bananas"
# print(reverse("I like apples and I also like bananas", "oranges")) # should return: "The word was not found"
# print(reverse("I like apples and I also like bananas", "Bananas")) # should return: "The word was not found"
# print(reverse("I like apples and I also like bananas", 3)) #should return: "invalid input" 
