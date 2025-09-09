## Free LLM Benchmark

## DISCLAIMER:
- **user is responsible** for the use of the software
- open router api key required (requires 10dollar account activation although the program doesnt use the credits you purchase in openrouter)
## how to run

- 1-run installer.bat to install python libraries

- 2-put this line of code in the cmd (Sh):
		setx OPENROUTER_API_KEY "your_api_key"
- 3-(optional)
	write questions in english or spanish inside peguntas_pendientes.csv (one question per line)
- 4-then run python script(Sh):
		python free_llm_tester.py
- 5-open html report in the /html/ folder using any browser

# more functionality
- html report generated for each question in /html/ dir
- xcel report generated in /xcell/ (BETA) (NOT WORKING)
- blacklist.csv to exclude free models from the benchmark
- failed reports go to /xcell_failed/ and /html_failed/
- successful queries go to "preguntas_resueltas.csv"
## Contributors
- **Francesc Miquel**
- **Germán Osorio**

This software has been developed for Rumi Project, allowing us to get free responses and compare intelligence.
