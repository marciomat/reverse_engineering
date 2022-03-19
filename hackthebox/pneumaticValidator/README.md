> source: [https://app.hackthebox.com/challenges/pneumatic-validator](https://app.hackthebox.com/challenges/pneumatic-validator)

# Files

Input:
- [pneumaticvalidator](pneumaticvalidator) - Original binary to crack

Output:
- [crack_passw.py](https://github.com/marciomat/reverse_engineering/tree/main/hackthebox/pneumaticValidator/crack_passw.py) - Python script to decrypt the password
- [func_simulation.c](https://github.com/marciomat/reverse_engineering/tree/main/hackthebox/pneumaticValidator/func_simulation.md) - Decompilation of the `simulation()` function

# The challenge

When we run the binary, it asks for the password to be passed as an argument.
And the first thing it does is validate the length:

```
$ ./pneumaticvalidator myPasswordAttempt   
Starting the Pneumatic Flag Validation Machine...
Wrong length
```

After opening the binary in radare2 we can easily see that we need 20 characters.
And this is what we get with the right lenght:

```
$ ./pneumaticvalidator myPasswordAttempt012
Starting the Pneumatic Flag Validation Machine...
Initializing Simulation...
Simulating...
Wrong \o\
```

# Solution

This challenge is quite hard. It has a *very* long and complex validation flow.

I spent few days looking at the assembly code, in radare2.
But after a while it was clear that I'd need a code with a higher level of abstraction, so I went with Ghidra instead.

Here is the `main()` function, decompiled by Ghidra:

> Note: functions were renamed by me, for clarity

```C
undefined8 main(int argc,long argv)
{
  undefined8 uVar1;
  size_t sVar2;
  float fVar3;
  int i;
  
  puts("Starting the Pneumatic Flag Validation Machine...");
  if (argc == 2) {
    sVar2 = strlen(*(char **)(argv + 8));
    if (sVar2 == 0x14) {
      process_passw(*(char **)(argv + 8),0x14);
      puts("Initializing Simulation...");
      malloc_global_vars();
      init_f_vector_sim();
      use_recursion_to_update_table();
      puts("Simulating...");
      for (i = 0; i < 1024; i = i + 1) {
        simulation();
      }
      fVar3 = get_max_f_vector_sim();
      if (15.0 <= fVar3) {
        puts("Wrong \\o\\");
      }
      else {
        puts("Correct /o/");
      }
      free_all_mallocs();
      uVar1 = 0;
    }
    else {
      puts("Wrong length");
      uVar1 = 1;
    }
  }
  else {
    puts("Please provide the flag to verify");
    uVar1 = 1;
  }
  return uVar1;
}
```

So far it doesn't look that bad. The problem is when we open the function `simulation()` to try to understand what's going on in there.

Here's just the first few lines. The pattern repeats throughout the function:

```C
void simulation(void)

{
  float fVar1;
  
  if (passw_vector_data_0x14x0x7[0][6] == 0) {
    fVar1 = 0.0;
  }
  else {
    fVar1 = 100.0;
  }
  f_vector_sim_0x8000_0x80x0x40[0x9b] = fVar1 + f_vector_sim_0x8000_0x80x0x40[0x9b];
  if (passw_vector_data_0x14x0x7[8][6] == 0) {
    fVar1 = 0.0;
  }
  else {
    fVar1 = 100.0;
  }
  f_vector_sim_0x8000_0x80x0x40[0xf9c] = fVar1 + f_vector_sim_0x8000_0x80x0x40[0xf9c];
  f_vector_sim_0x8000_0x80x0x40[0x1439] = f_vector_sim_0x8000_0x80x0x40[0x1439] + 100.0;
  if (passw_vector_data_0x14x0x7[11][6] == 0) {
    fVar1 = 0.0;
  }
  else {
    fVar1 = 100.0;
  }
  f_vector_sim_0x8000_0x80x0x40[0xfe1] = fVar1 + f_vector_sim_0x8000_0x80x0x40[0xfe1];
  f_vector_sim_0x8000_0x80x0x40[0x532] = f_vector_sim_0x8000_0x80x0x40[0x532] + 100.0;
```

> The entire function is [here](https://github.com/marciomat/reverse_engineering/tree/main/hackthebox/pneumaticValidator/func_simulation.md).

And to make it more complicated, this function `simulation()` is executed 1024 times!

## Black-box attempt

I spent most of my time renaming functions, re-assigning variable types (so Ghidra shows the right array format) and trying to have a better picture of how the validation works.

In the end it was clear that I had no chance to understand the entire validation flow.

Another approach for this kind of problem is to consider the entire validation as a black-box.
We just look at the inputs and outputs, and try to keep track of how the former affects the latter.

There are a few qualities of the validation method that makes it harder or easier to use this technique:

- Control over all inputs: If there is any input that we can't control (e.g. if time of the day is used to scramble the data) it will make it much harder

- Validation of inputs made independently: An example of inputs validated independently is if the binary looks for a letter 'A' in position 1. On another hand, the binary may take the entire input string, calculate the SHA-256 and compare with the expected result. This would make it much harder

- How fast is the validation: If the validation of the password takes 3h, it would be a very long process to attempt a try-and-error approach, possibly making it impossible

So how this binary fits in this analysis?

- We have control over all inputs. By looking at the binary we can be sure it only cares about the password.
- The characters of the password are *not* validated independently. So this will make the process a bit harder.
- The validation takes about 4 seconds each run. Not bad but it will take quite a while to brute-force all 20 characters.

## Ready or not, here I come!

Even though the input characters are not validated independently, there is one thing that will help us make sure we're heading in the right diretion.

Let's look again at the final check in the `main()` function:

```C
      puts("Simulating...");
      for (i = 0; i < 1024; i = i + 1) {
        simulation();
      }
      fVar3 = get_max_f_vector_sim();
      if (15.0 <= fVar3) {
        puts("Wrong \\o\\");
      }
      else {
        puts("Correct /o/");
      }
```