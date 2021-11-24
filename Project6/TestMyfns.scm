#!/usr/bin/env scheme-srfi-7

(program
  (requires srfi-34 srfi-78)
  (files "myfns.ss")
  (code

(define myinterpreter-with-exception-handling
  (lambda (progs)
    (call-with-current-continuation
      (lambda (k)
        (with-exception-handler
          (lambda (x)
            (display x)
            (newline)
            (k "Error")
			(newline))
          (lambda () (myinterpreter progs)))))))

(define (main args)
  (check-set-mode! 'report-failed)
  (display "Grading myfns.ss")
  (newline)

	(check (myinterpreter-with-exception-handling
           '(prog 10))
         => 10)
	
	(check (myinterpreter-with-exception-handling
           '(prog (myadd 1 2)))
         => 3)
	
	(check (myinterpreter-with-exception-handling
           '(prog (mymul 2 5)))
         => 10)
		 
	(check (myinterpreter-with-exception-handling
           '(prog (mysub 0 10)))
         => -10)
		 
	(check (myinterpreter-with-exception-handling
           '(prog (myif 0 5 10)))
         => 10)
		 
	(check (myinterpreter-with-exception-handling
           '(prog (mylet x 10 (myadd x x))))
         => 20)
		 
	(check (myinterpreter-with-exception-handling
           '(prog (myadd 10 (mylet x 5 (mymul x x)))))
         => 35)
		 
	(check (myinterpreter-with-exception-handling
           '(prog (mylet x (mysub 0 (mylet x 10 x)) (myadd x (mylet x 1 (myadd x x))))))
         => -8)
		 
	(check (myinterpreter-with-exception-handling
           '(prog (mylet x (mysub 0 (myadd 10 11)) (mylet y x (mymul x y)))))
         => 441)
		 
	(check (myinterpreter-with-exception-handling
           '(prog (myif (myadd 0 1) (mylet x 10 x) (mylet x 15 x))))
         => 10)
		 
	(check (myinterpreter-with-exception-handling
           '(prog (mylet a (myfunction b (myadd b b)) (a 5))))
         => 10)
		 
	(check (myinterpreter-with-exception-handling
           '(prog (mylet a (myfunction b (myadd b b)) (mylet a 1 (mymul a a)))))
         => '1)
		 
	(check (myinterpreter-with-exception-handling
           '(prog (mylet f (myfunction x (myadd 10 x)) (f 5))))
         => '15)
		 
	(check (myinterpreter-with-exception-handling
           '(prog (mylet f (myfunction x (myadd 10 x)) (f (f 5)))))
         => '25)

  (display "Result:")
  (check-report))))