---
layout: post
title: "Product Thinking"
date: 2017-09-13 11:52
---

As a PhD student focusing on limited academic fields, to be honest,
I've not worked for any product-driven companies. For a long time, I
am curious about how a product is designed, implemented and finally
comes out. And I am very passionate about making things like writing
academic papers. On this weekend, I take a little step on this by
implementing my own "product" from scratch. This is really a unique
experience and I would have done this earlier when I'm still in
college. Below is the whole story.

## Motivation

I've been a big fan of [Instapaper](https://www.instapaper.com/) since
I switched from [Pocket](https://getpocket.com/) years ago. Basically,
it is excellent for its beautiful design, e.g., interaction,
typography, color themes. And, since it is acquired by
[Pinterest](http://pinterest.com), we can take unlimited highlights or
notes for free while reading articles (It is a premium feature before
the acquisition.) so it becomes a totally free service. For
comparison, Pocket, known as Instapaper's main competitor, gets native
advertising for profit. I have to say such advertising is really a
catastrophe for this kind of services.

Since my first try, every tiny detail of Instapaper has attracted me
more or less. Among them, a seemingly insignificant feature called
[Tweet
Shots](https://medium.com/making-instapaper/instapaper-tweet-shots-5df8587988e8)
really surprises me. Its basic functionality is really simple: making
images from highlighted texts. Below is the resulting image generated
in Instapaper for iOS. Yes, this idea is from the CEO John Borthwick.

![Instapaper's Tweet shots.](/assets/img/20170913-1.jpg)

Such a simple but awesome idea this is! I cannot love it more and
actually I wish it could be published as another product
individually. After searching on internet, I find some similar ideas,
e.g., [src2png](https://github.com/mplewis/src2png),
[text2image](http://www.text2image.com/) and
[node-canvas-text](https://github.com/kaivi/node-canvas-text). None of
these looks like what is in my mind so I decided to Do It Myself.

## Prototyping

To start with, like writing a research paper, I design an overview of
my product. A name? No, I am not ready for entrepreneurship and this
article is not a product handbook for professionals. Therefore, I skip
/the art of product naming/ and just casually call my product "zQuote"
because it uses texts to make images like quotation cards. Then,
instead of considering cross-platform, mobile friendly and etc, I
target the terminal, i.e., Command Line Interface (CLI). I scribble an
expected prototype below.

![zQuote prototype](/assets/img/20170913-2.jpg)

From a user's perspective, the core functionality of zQuote is as easy
as taking screenshots and then do some image crops. However, taking
screenshots cannot ensure consistent visual experience, e.g.,
typography. Moreover, it can hardly be integrated with other
programs. Thus, in my opinion, this is not an alternative solutions to
be considered.

## Tech Stack

Then, for determining the tech stack, the first tool coming into my
mind is $\LaTeX$. It is a reliable tool for generating steerable and
high-quality documents so I can afterwards convert the results, e.g.,
pdf, into image formats using
[ImageMagick](http://imagemagick.org). However, it is more like a
dirty hack than a feasible solution.

Then, I consider [OpenCV](http://opencv.org) as I have some pleasant
experience of processing images using it. However, it is dedicated for
computer vision and has few functionalities for typography. It does
not seems to be a good choice either.

[Cairo](https://www.cairographics.org) is a 2D graphics library with
support for multiple output devices. I heard this program before when
I use [gnuplot](http://www.gnuplot.info). It seems good for processing
text rendering and it can also generate image files in "png" format. I
take a quick try and it indeed performs well in converting text into
images. However, the biggest problem is that it does not support line
wrap which is a critical requirement in zQuote. Therefore, I try to
manually calculate the width of every single character, hoping to
realize a hard line wrap. However, I have to admit that I overestimate
this issue. Chinese characters and English letters have different
width and it seemingly relates to font family too. Even for the whole
English texts, line wrap is a challenge when considering letter, word
and hyphen. Fortunately, I find [Pango](https://www.pango.org) which
is a library for laying out and rendering of text. Also, it considers
internationalization. As it is said on Pango's official site, the
integration of Pango with Cairo provides a complete solution with high
quality text handling and graphics rendering. I try it out and it
works like a charm including line wrap.

Finally, the tech stack is set as Pango with Cairo in C programming
language as both of them are written in C.

## Challenges

Actually, using Pango with Cairo solves most challenges including line
wrap and internationalization problem. However, there is also a
challenge which makes precisely controlling margins tricky. On the one
hand, a fixed size has to be specified for creating a new surface
before rendering text. On the other hand, the size of the text area is
unknown unless a surface is available. This is really a
contradiction. Luckily, Cairo supports a special surface called
"recording surface" of undefined size. Such surface can record all the
operations of text rendering and layout. It is easy to map it to
a normal surface after the size of text area is calculated on the
"recording surface".

## Promotion

I am not ready for this step yet but the whole repository of this
project is on [Github](https://github.com/gujiaxi/zQuote). Below are
some sample results.

![Sample zQuote results-1](/assets/img/20170913-3.jpg)

![Sample zQuote results-2](/assets/img/20170913-4.png)

## Conclusion

Making product is different from doing academia. I conclude several
humble thoughts through my experience of zQuote:

1. Start from a little, humble, insignificant idea.
2. Never underestimate the cost of realizing a seemingly simple idea
   before you start.
3. Forget about those dirty hacks and find the dedicated stepping
   stones.
4. Divide your product into simple pieces and conquer them one by one,
   step by step.
