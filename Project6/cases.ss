;; Test Cases for the project

; Use this file for testing individial cases
; Use the file TestMyfns.scm to test all the cases at once
; Start the interpter and load this file using the command 
;  ,load cases.ss 
; or the command
;  (load "cases.ss")
; After they are loaded, you can test your interpeter using this command:
;  (myinterpreter c1)
; To get a list of the expected outputs for cases c1-c14, use this command:
;  official

(define c1 '(prog 10))
(define c2 '(prog (myadd 1 2)))
(define c3 '(prog (mymul 2 5)))
(define c4 '(prog (mysub 0 10)))
(define c5 '(prog (myif 0 5 10)))
(define c6 '(prog (mylet x 10 (myadd x x))))
(define c7 '(prog (myadd 10 (mylet x 5 (mymul x x)))))
(define c8 '(prog (mylet x (mysub 0 (mylet x 10 x)) (myadd x (mylet x 1 (myadd x x))))))
(define c9 '(prog (mylet x (mysub 0 (myadd 10 11)) (mylet y x (mymul x y)))))
(define c10 '(prog (myif (myadd 0 1) (mylet x 10 x) (mylet x 15 x))))
(define c11 '(prog (mylet a (myfunction b (myadd b b)) (a 5))))
(define c12 '(prog (mylet a (myfunction b (myadd b b)) (mylet a 1 (mymul a a)))))
(define c13 '(prog (mylet f (myfunction x (myadd 10 x)) (f 5))))
(define c14 '(prog (mylet f (myfunction x (myadd 10 x)) (f (f 5)))))


; Here are the correct outputs for each case, from c1-c14
(define official '(10 3 10 -10 10 20 35 -8 441 10 10 1 15 25))