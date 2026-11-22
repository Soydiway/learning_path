# Study Progress & Code Dump

This is just a repository for tracking my learning milestones. Some of the tasks here are self-assigned, while others are part of my study plan. Not that it matters—the main point is simply documenting my progress. That way, in the near future, I can look back at this repo and say, *"Man, what an idiot I was."* Until then, I'll keep writing random stuff and pushing it here.

Oh, and I'm also practicing Git, so don't judge me too harshly for poorly styled commits, a messy repo, or writing code worse than your late grandpa... I'm still a beginner, okay? Come back in, like... 45 years—maybe I'll be a master by then.

## About the Files

I don't see the point in explaining what every single program does—as long as you have neither more nor fewer than 46 chromosomes, you can figure it out just from the file names (well, except for the files in the `python` folder; I'm already lost in there myself).

## Compilation Note

However, I do want to point out that `extended_calcu_module.c` is a module used by another program, `console_menu.c`. Make sure to compile them together:

```bash
gcc c/exercises/fun_programs/console_menu.c c/exercises/calculators/extended_calcu_module.c -o app
`
Otherwise, you'll be violating the international law of the Criminal Code of Planet Earth's quantum... go fuck yourself
