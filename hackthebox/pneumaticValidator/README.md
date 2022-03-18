> source: [https://app.hackthebox.com/challenges/pneumatic-validator](https://app.hackthebox.com/challenges/pneumatic-validator)

# Files

Input:
- [pneumaticvalidator](pneumaticvalidator) - Original binary to crack

Output:
- [crack_passw.py](https://github.com/marciomat/reverse_engineering/tree/main/hackthebox/pneumaticValidator/crack_passw.py) - Python script to decrypt the password
- [func_simulation.c](https://github.com/marciomat/reverse_engineering/tree/main/hackthebox/pneumaticValidator/func_simulation.md) - Decompilation of the `simulation()` function

# The challenge

When we run the binary, it asks for the password to be passed as an argument.
And the first thing it does is validate the legnth:

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

Here's just the first few lines, to get an idea of the size of the trouble we are in:

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

And to make it even worse, this function `simulation()` is executed 1024 times!

## Two steps forward, two steps back

I spent most of my time renaming functions, re-assigning variable types (so Ghidra shows the right array format) and trying to have a better picture of how the validation works.
