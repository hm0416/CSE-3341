class Scanner {
    BufferedReader file = null;
	// Constructor should open the file and find the first token
	Scanner(String filename) {
		file = new BufferedReader(new FileReader(new file(filename)));
		nextToken();
	}

	// nextToken should advance the scanner to the next token
	public void nextToken() {
	    //"hi my name is" - break it up
	    List<String> allLines = new LinkedList<String>;
	    String singleLine = null;
        while(singleLine = file.readLine() != null) {
            allLines.add(singleLine);
        }

        //pop out each item in list, so each item is a sentence kinda
        //split the sentence so tokenizes

		
	}

	// currentToken should return the current token
	public Core currentToken() {
		return 0;
	}

	// If the current token is ID, return the string value of the identifier
	// Otherwise, return value does not matter
	public String getID() {
		return "";
	}

	// If the current token is CONST, return the numerical value of the constant
	// Otherwise, return value does not matter
	public int getCONST() {
		return 0;
	}

}