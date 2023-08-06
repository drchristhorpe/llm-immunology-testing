# Testing LLMs with immunological questions/prompts

## Aim
The aim of this project is to understand where LLMs either inform well or mis-inform.

It will look systematically at the responses to a set of prompts each of which contains a specific question (or sometimes two).

This hopefully will give some information on what sorts of questions can be reliably answered and which cannot. 

This will help immunologists and teachers/students of immunology understand how the can use LLMs in their research and study.

## Dependencies

The project relies upon the ['llm'](https://github.com/simonw/llm) Command Line Utility (CLI) and Python library

The project also depends on the `toml` python library.

## Files not included in the repository

Is a configuration file, config.toml. This is excluded as it includes the OpenAI API key. To use the repository create this file in the root directory and include these two properties in the file

"OPENAI_API_KEY"="my-secret-openai-api-key-goes-here"
"ITERATIONS"=10

## TODO list

- write functionality/questions where data is returned in JSON notation for some questions
- write functionality to not repeat work already done
- unit tests and test runners





