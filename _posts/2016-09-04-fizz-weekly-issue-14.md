---
layout: post
title: "Fizz Weekly Issue #14"
date: 2016-09-04 20:29
---

## 睹·Reads

- [Why I started learning Emacs in 2016](http://www.warski.org/blog/2016/08/why-i-started-learning-emacs-in-2016/)

  2016，选择Emacs的理由。

- [more, less, and a story of typical Unix fossilization](https://utcc.utoronto.ca/~cks/space/blog/unix/MoreAndUnixFossilization)

  Unix中`more`跟`less`的故事。

- [复古像素：游走在方寸间的艺术](http://toutiao.com/a4423189506/)

  艺术不局限于技术。

- [Repl Electric - Live Coding](http://www.repl-electric.com/)

  基于Emacs的代码表演。

## 研·Researches

- *Advanced Transport Options for the Dynamic Adaptive Streaming over HTTP* [^1]
  - 早期的HTTP协议并没有规定网络层协议，虽然现在大部分实现都是用TCP的。TCP的问题是可靠传输导致的效率低下，这对视频流播服务是致命的；近年来有些文章已经开始探索其他协议，比如说HTTP/2还有基于UDP的QUIC协议；研究表明基于TCP的视频流带宽需要达到视频码率的两倍才行；HTTP 1.1开始引入了persistent和pipeline的特性。

- *Live streaming of 4K ultra-high definition video over the internet* [^2]
  - 这篇文章主要结合了HTTP/2和OpenFlow来解决延迟跟启动的问题，针对的是超高清视频直播，不过本文只有4页，只是从概念上证明了可行性，并未给出实际的实验结果。

- *An HTTP/2 push-based approach for SVC adaptive streaming* [^3]
  - SVC最大的缺点是它使每一层的编码开销变多了10%，从而使得需要传输更多的比特。MUELLER et al. 首次探索了SPDY用于自适应码率流播，但是他们发现该方法的几大优势都被SPDY所强制要求的SSL以及成帧的额外开销所抵消了。Wei et al. 使用了HTTP/2，利用push特性来减小延迟，并把segment的大小从5秒减小到了1秒，最终的延迟从16秒减小到了4秒。

## 思·Thoughts

> We escape into truisms, small talk and distractions. Given the opportunity at a family gathering to share our hopes and disappointments, we talk about the weather and watch TV.

-----

[^1]: Timmerer, Christian, and Alan Bertoni. "Advanced Transport Options for the Dynamic Adaptive Streaming over HTTP." arXiv preprint arXiv:1606.00264 (2016).
[^2]: Petrangeli, Stefano, et al. "Live streaming of 4K ultra-high definition video over the internet." Proceedings of the 7th International Conference on Multimedia Systems. ACM, 2016.
[^3]: van der Hooft, Jeroen, et al. "An HTTP/2 push-based approach for SVC adaptive streaming." NOMS 2016-2016 IEEE/IFIP Network Operations and Management Symposium. IEEE, 2016.
