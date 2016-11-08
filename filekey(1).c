#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <evp.h>
#include <ctype.h>

void pad(char *s, int length);
int print_result(unsigned char *buf, char *s, int len, FILE *outFile, char *match);
int strcicmp(char const *a, char const *b);

int main()
{
	unsigned char match[] = "BINGO";
	unsigned char no_MATCH[] = "NO MATCH";
	int i;
	char words[16],t;//each word in the dictionary
	FILE *key, *outFile;
	unsigned char outbuf[1024 + EVP_MAX_BLOCK_LENGTH];
	unsigned char iv[16] = {0}; //given in the description of the task 5
	int outlen, tmplen;
	int num;
	
	EVP_CIPHER_CTX ctx;
	EVP_CIPHER_CTX_init(&ctx);
	char inText[] = "This is a top secret."; //given in the description of task 5
	char cipherTextGiven[] = "8d20e5056a8d24d0462ce74e4904c1b513e10d1df4a2ef2ad4540fae1ca0aaf9";
	key = fopen("amey.txt", "r"); //Dictionary words for matching
	if( remove("matchingResult.txt") == -1)
	{
		perror("Error Deleting file");
	}
	outFile = fopen("matchingResult.txt", "a+");
	if( key <0 || outFile <0)
	{
		perror("cannot open file");
		exit(1);
	}
	char pbuffer[1024];
	
	//int count;
	while( fgets(words, 16, key)) //get each word from dictionary that suppose to be a key to encrypt
	{
		i = strlen(words);
		words[i-1] = '\0'; // in the text editor it automatically adds null or end of file so we need to remove that 
		i = strlen(words);
		if(i<16) //16 because we use AES-128
		{ //Since the word has less than 16 characters, space characters are 
			// are appended to the end of the word to form a key of 128 bits
			pad(words, (16));	
		}
		EVP_EncryptInit_ex(&ctx, EVP_aes_128_cbc(), NULL, words, iv);
		if(!EVP_EncryptUpdate(&ctx, outbuf, &outlen, inText, strlen(inText)))
		{
			EVP_CIPHER_CTX_cleanup(&ctx);
			return 0;
		}
		if(!EVP_EncryptFinal_ex(&ctx, outbuf + outlen, &tmplen))
		{
			EVP_CIPHER_CTX_cleanup(&ctx);
			return 0;
		}
		outlen += tmplen;
		
		int i;
		char* buf_str = (char*)malloc(2*outlen +1);
		char* buf_ptr = buf_str;
		for(i=0;i<outlen;i++)
		{
			buf_ptr += sprintf(buf_ptr, "%02X", outbuf[i]);
		}
		*(buf_ptr +1) = '\0';
		if(strcicmp(cipherTextGiven, buf_str) ==0)
			print_result(outbuf, words, outlen, outFile, match);
		else
			print_result(outbuf, words, outlen, outFile, no_MATCH);
	}
	fclose(key);
	fclose(outFile);
	return 1;
}

 //print result to output file matchResult.txt
 int print_result(unsigned char *buf, char *s, int len, FILE *outFile, char *match)
 {
	 int i,n,j,k;
	 char x='\n';
	 char space = ' ';
	 for(j=0;j<strlen(s);j++)
	 {
		 fprintf(outFile,"%c",s[j]);
	 }
	 fprintf(outFile, "%c", space);
	 for(i=0;i<len;i++)
	 {
		 fprintf(outFile,"%02x",buf[i]);
	 }
	 fprintf(outFile, "%c", space);
	 for(k=0;k<strlen(match);k++)
	 {
		 fprintf(outFile,"%c",match[k]);
	 }
	 fprintf(outFile, "%c",x);
	 return(0);
 }
 
 //add padding to the key
 void pad(char *s, int length)
 {
	 int l;
	 l=strlen(s); //its length
	 while(l<length)
	 {
		 s[l] = ' ';  //insert a space
		 l++;
	 }
	 s[l] = '\0';  //strings need to be terminated in a null
 }
 
 //compare case insensitive
 int strcicmp(char const *a, char const *b)
 {
	for (;;a++,b++)
	{
		int d = tolower(*a)-tolower(*b);
		if(d!=0 || !*a)
			return d;
	}		
 }
