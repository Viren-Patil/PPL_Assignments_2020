(terpri)
(princ "Program to calculate factorial of a number iteratively and then display it.")
(terpri)
(princ "Enter the number: ")
(setq n (read))
(defvar fac 1)
(loop
	(setq fac (* fac n))
	(decf n 1)
	(when (= n 1) (return fac))
)
(princ "The factorial is: ")
(write fac)

