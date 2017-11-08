BEGIN{
i=1;}
{
S[i] = $1;
i = i+1;

}
END{
printf("%s\t%2f\n",S[1],S[4]);}
