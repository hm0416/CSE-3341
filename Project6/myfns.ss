; ;Author: Hifa Mousou
; Project 6 

(define emptyList '()) ;inital list to pass into the execExpr function

(define (myinterpreter program)    
	;checks if first element starts with prog, if it does gets everything after the prog keyword and calls execExpr on it
    (if (equal? (car program) 'prog)(execExpr (cadr program) emptyList) 0 ))

(define (execExpr expr list)
	(cond
	((symbol? expr) (getIDVal expr list)) ;gets the ID value
	((integer? expr) expr) ;return const if expr is an integer
	((equal? (car expr) 'myif) (execMyIf (cdr expr) list)) ;if first element is the myif function then call myif on the rest of the args
	((equal? (car expr) 'myadd) (execMyAdd (cdr expr) list)) ;if first element is the myadd function then call myadd on the rest of the args
	((equal? (car expr) 'mymul) (execMyMul (cdr expr) list)) ;if first element is the mymul function then call mymul on the rest of the args
	((equal? (car expr) 'mysub) (execMySub (cdr expr) list)) ;if first element is the mysub function then call mysub on the rest of the args
	((equal? (car expr) 'mylet) (execMyLet (cdr expr) list)) ;if first element is the mylet function then call mylet on the rest of the args
	((equal? (car expr) 'myfunction) expr))) ;if first element is the myfunction function then return 
	; ((symbol? (car expr)) (execFuncCall expr list)))) ;if first element is a symbol then there is a function being called


;Executes myadd
(define (execMyAdd expr list)
	(if (null? expr) 
		0
		(+ (execExpr (car expr) list) (execMyAdd (cdr expr) list))))
		
;Executes mysub
(define (execMySub expr list)
	(if (null? expr) 
		0
		(- (execExpr (car expr) list) (execMySub (cdr expr) list))))
		
;Executes mymul
(define (execMyMul expr list)
	(if (null? expr) 
		1
		(* (execExpr (car expr) list) (execMyMul (cdr expr) list))))
		
(define (getIDVal id list)
	(if (equal? id (car (car list))) (cdr (car list)) (getIDVal id (cdr list))))


(define (execMyIf expr list)
	(if (equal? (execExpr (car expr) list) 0) ;checks if first expr is zero
	(execExpr (caddr expr) list) ;if it's zero then return third expr
	(execExpr (cadr expr) list))) ;otherwise return the second expr because expr is non-zero
	

(define (execMyLet expr list)
	(execExpr (caddr expr) (cons (cons (car expr) (execExpr (cadr expr) list)) list)))


; (define (execFuncCall expr list))
