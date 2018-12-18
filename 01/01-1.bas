   10 CLEAR 49151
   20 LOAD ""CODE 49152
   30 LET total=0
   40 LET address=49152
   50 LET s$=""
   60 LET c$=CHR$ PEEK address
   70 LET address=address+1
   80 IF c$=CHR$ 10 THEN GO TO 110
   90 LET s$=s$+c$
  100 GO TO 60
  110 LET total=total+VAL s$
  120 IF address<52614 THEN GO TO 50
  130 PRINT total
