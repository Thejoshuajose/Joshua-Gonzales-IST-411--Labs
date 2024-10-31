# Project: Lab 9 HMAC
# Purpose Details: Learning how to use HMAC Hashing and Message Authentication Code
# Course: IST 411
# Author: Joshua Gonzales
# Date Developed: 10/22/2024
# Last Date Changed: 10/22/2024
# Rev:1

import hashlib
import hmac
import base64
import json

message1 = '{"Name":"Josh"}'
key1 = "This is the key"

message2 = '{"Name":"James"}'
key2 = "This is a different key"

message3 = '{"Name":"Josh"}'
key3 = "This is the key"


def generate_sig(message,key):
	message_enc = message.encode('utf-8')
	key_enc = key.encode('utf-8')
	print("\nEncoding Message and Key...")
	digesterSHA1 = hmac.new(key_enc, message_enc, hashlib.sha1)
	print("Creating SHA1 Signature...")
	SHA1signature = digesterSHA1.digest()
	print("Creating MD5 Signature...")
	digesterMD5 = hmac.new(key_enc, message_enc, hashlib.md5)
	MD5signature = digesterMD5.hexdigest()
	print("Creating Base64 Signature...")
	encoded_sig = base64.urlsafe_b64encode(SHA1signature)
	print("SHA1 Signature: ",SHA1signature)
	print("MD5 Signature: ", MD5signature)
	Base64signature = encoded_sig
	print("Base64 Signature: ",Base64signature)
	return encoded_sig

def compare_sig(sig1,sig2):
	print("\nComparing Signatures....")
	print("Signature 1: ", sig1)
	print("Signature 2: ", sig2)
	print(hmac.compare_digest(sig1, sig2))
	return hmac.compare_digest(sig1, sig2)

try:
	sig1 = generate_sig(message1,key1)
	sig2 = generate_sig(message2,key2)
	sig3 = generate_sig(message3,key3)

	compare_sig(sig1,sig2)
	compare_sig(sig1,sig3)
except Exception as e:
	print(e)
