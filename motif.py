import random
l=int(input("Enter the length of motif :"))
file=open("sequence.txt")
r=file.read()
print("Sequence",r)
size=len(r)
print("Size of the sequence",size)
pos=random.randint(0,len(r)-5)
#pos = 1
print("Position",pos)
motif=r[pos:pos+l]
print("Motif",motif)
i=pos+1
while(i<=size-1):
    if(motif==r[i:i+1]):
        str1=r[i:i+1]
        print("Match motif",str1)
        file1=open("motooutput.txt","a")
        file1.write(str1+" ")
    i+=1


 output:
 >
Enter the length of motif :4
Sequence 
AACCACGTACACAAGATTTCAACATTTATATGTGTCAACATGAGACTTTTCATCACCTAATTATATCAAT
ATAATACCTATTGAGTATTAGATATTGACCCTTACAACATCCGACATCTATTTCATTCCTCTGAAATATA
AGTTGTATTATTTTTATCCGAGTGGTTAGGTTGGAAAATAATAAAATGCTTAAGAAATAAACTTAAGAGG
AAAGGAAACATAAAACAAATAGAAAAAGGAACTTTATTTGGCTTGGTCCATATGCTTATCATCCTAGCTT
CTCTGTTACTATCTTCTTTTTCCCTTAACTTTTTTTTCTTTTTCATGTATAATCAAACTTCTCTCGACAA
TATTCTTCTTTATAATCATACTTTATTATAGCAATTTTATTTTTTGCTATATTATATTATAGTATATACC
CTCTTATGTGAGACAGCAAAAAATGTAAATGAATAATTAAACTTGCAGAATTAGATTTGAAAGATATTTT
TCATGTTTTTTTGCGGGTCAAATCATTCATTAAGAGCCTAGATGTACTACGTGCAACTTCTTAACCTTTC
TAAGACTAAATCAAGGAATTGGGAAAGAACAAAAATACACGTAAAACTGGGATTTTGTACAGCCCATTAA
ATTAGTTTTATCATTTGAAATTAGACAAGAGGAATAATGAATTTTAGCTATTCTTGTTCCTAACCCTATC
ACACAAATTTTCTCAGATCCCTTTCAAATTAATATCTTCTTAACTAAACATCATGTATGACTTATATACA
CCACAATATGAATTAAGAAGATACTGAAAAATTAAGGAATTGTTGACTAAATTTTAAGTCAAAGGACCAT
ATCTTGAGTGGAAATTTCTAAGAAATATCGTATTCAGTACATATATGATTACTTTAAGTAAGGTATTGCC
AAAACGCAACCGTGTCTTTTCTAACAACATAAAAACACGGCATTTTCTACTAATCAATCCGCTTTTGTTT
ACCAATTCTACAATTCAAACCCTACACATATAGTATACACATTAAACCAAAGACTGAAACGACACCTATA
TATATTCAACTCCACGTACCAAAGGATACTCATCTCTATTATTATTGCATCCTATACATATACTAAAAGG
GCAAAGCAATATAATCTGTACTTTATTTTTCTTGAGCC


Size of the sequence 1177
Position 470
Motif TGCA