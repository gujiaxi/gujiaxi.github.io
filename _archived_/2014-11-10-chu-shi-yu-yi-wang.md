---
layout: post
title:  "初识语义网"
date:   2014-11-10
---
> If HTML and the Web made all the online documents look like one huge book, RDF, schema and inference languages will make all the data in the world look like one huge database.
> 
> --- Tim Berners-Lee, Weaving the Web, 1999

最近因为某课程的关系看了一些语义网相关的文章，在这里总结一下，欢迎指正。

## 概念
语义网（[Semantic Web](http://en.wikipedia.org/wiki/Semantic_Web)）的概念由[Tim Berners-Lee](http://en.wikipedia.org/wiki/Tim_Berners-Lee)在1998年提出。它的基本概念是说创造一种计算机能够理解的智能网络，实现人与计算机之间无障碍地沟通。想像在未来某一天你只要打开网页输入“帮我订明天早上去北京的机票”，然后计算机就立马帮你提供一条龙服务：设置闹铃、挑选航班、规划行程（包括酒店）、支付费用……

## 特征
我们知道，现在使用的万维网其实就是由一堆文本（e.g. html）组成的（感觉超文本的出现已经跨出了很大一步了，它使得信息能够链接起来形成大的数据网），计算机所能看到的只是文本数据，而对于其内容无法理解，也就是说要从**数据（Data）**中萃取出**信息（Information）**进而形成**知识（Knowledge）**还要我们人来参与，这就是传统的万维网，它主要是供人阅读、交流和使用的，其主要任务就是信息发布与获取。通过在网络上发布或获取信息来达到共享和交流的目的。而语义网的主要任务则是计算机之间的相互交流和共享，从而使计算机可以代替人们完成一部分工作，使网络应用更加智能化、自动化和人性化。

## 结构
相对于传统的网络来说，语义网除了要解决上面提到的“计算机无法理解内容”一个问题，还有一个严重的问题是网络上大量无序的信息，它们在内容上的联系很难建立（信息孤岛）。因此语义网的设计抛开了传统的网页之间的关系，通过语义来建立事物之间的关系。下图是2000年提出的语义网层次模型：

![](/assets/img/20141110-1.png "Semantic Web")

## 模型
前面也已经说到，传统的万维网是建立在文档的基础上的，而文档各自包含丰富的内容（事物），怎样使内容（事物）能够从传统的文档中解放出来，建立内容之间的联系呢，就需要一个特定的模型来描述及组织事物，说到这里，其实不同的学派在这个问题上差异很大，比较全面的应该是W3C的[RDF](http://en.wikipedia.org/wiki/Resource_Description_Framework)。RDF可被用于表达关于任何可在Web上被标识的事物的信，它基于这样的思想：用[URI](http://en.wikipedia.org/wiki/Uniform_resource_identifier)（可以算是URL的超集）来标识事物，用简单的属性及属性值来描述资源。这使得RDF可以将一个或多个关于资源的简单陈述表示为一个由结点和弧组成的图（[Named graph](http://en.wikipedia.org/wiki/Named_graph)）。RDF用一套特定的术语来表达陈述中的各个部分。确切地说，关于事物的陈述中用于识别事物的那部分就叫做主体（Subject），而用于区分陈述对象主语的各个不同属性的那部分就叫做谓词（Predicate），陈述中用于区分各个属性的值的那部分叫做客体（Object）。

除了上面提到的RDF，还有一个关键模型叫做Ontology（本体？叔本华？），它是在RDF基础上定义的概念及其关系的抽象描述，用于描述应用领域的知识，描述各类资源及资源之间的关系，实现对词汇表的扩展。

## 应用
其实广义来说，我们用了很多年的RSS，还有现在的Apple Siri，Google Now……都跟语义网有所关联，无形之中都渗透到我们的生活中了，虽说语义网还有很长的一段路要走，但是就现在来说，很多公司都在探索，应用主要围绕个性化服务、语义搜索、知识库这几个方面。具体的可以看文末的参考链接。

<center><iframe src="//commons.wikimedia.org/wiki/File:Linked-open-data-Europeana-video.ogv?embedplayer=yes" width="640" height="480" frameborder="0" webkitAllowFullScreen mozallowfullscreen allowFullScreen></iframe></center>

## 前景
就目前来说，语义网确实面临不小的挑战，除了技术问题，还有很多社会问题（个人隐私、知识产权、商业利益……）有待进一步解决。未来会怎样，还不能过早定论。最后引用一下某位大牛的预言，未来的互联网必然朝两个维度发展：向社会化发展——连接人与人；向语义化发展——连接知识与知识，最终达到[The Ubiquitous Web](http://www.w3.org/UbiWeb/)（没错，文章开头说的某课程就是普适计算）。

-----

- [The Semantic Web](http://isel2918929391.googlecode.com/svn-history/r347/trunk/RPC/Slides/p01_theSemanticWeb.pdf)
- [RDF 1.1 Concepts and Abstract Syntax](http://www.w3.org/TR/2014/REC-rdf11-concepts-20140225/)
- [Semantic Web Services](http://www.computer.org/csdl/mags/ex/2001/02/x2046.pdf)
- [Semantic linking through spaces for cyber-physical-socio intelligence: A methodology](http://www.sciencedirect.com/science/article/pii/S0004370211000208)
- [Semantic Web Patterns: A Guide to Semantic Technologies](http://readwrite.com/2008/03/25/semantic_web_patterns)
- [Top 10 Semantic Web Products of 2010](http://readwrite.com/2010/12/29/top_10_semantic_web_products_of_2010)
- [The Linking Open Data cloud diagram](http://lod-cloud.net/)
- [顶级专家Frank van Harmelen揭秘语义网](http://www.few.vu.nl/~FAH.van.Harmelen/popularising/C-T07-Chinese.pdf)
- [黄智生博士谈语义网与Web 3.0](http://www.infoq.com/cn/articles/semantic-web-and-web3)
- [知识图谱：大数据语义链接的基石](http://bcs.duapp.com/cips-upload/kg2/kg2_ljz.pdf)
