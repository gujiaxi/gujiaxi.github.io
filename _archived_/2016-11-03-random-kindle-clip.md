---
layout: post
title: "Random Kindle Clip"
date: 2016-11-03 11:36
---

Use awk to generate a random quote from your *My Clippings.txt*.

``` awk
BEGIN {
  clipping = "";
  i=0;
  flag=1;
  srand();
}
{
  if ($0 !~ /==========/) {
    if ($0 !~ /^-\s+/) {
      if ($0 !~ /^\s*$/ ) {
        if (clipping == "") {
          clipping = "--- " $0;
        } else {
          clipping = $0 "\n\n" clipping;
        }
      }
    }
  } else {
    clippings[i++] = clipping;
    clipping = "";
  }
}
END {
  print clippings[int(rand()*i)];
}
```

An example of the output is as follows:

> A programming language is for thinking of programs, not for expressing programs you've already thought of. It should be a pencil, not a pen.
> 
> --- Hackers & Painters (Paul Graham)