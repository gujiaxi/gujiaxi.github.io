---
layout: post
title: "学习ggplot2"
date: 2014-11-05
---
# 点、线、条形图
```r
library(ggplot2)
qplot(pressure$temperature, pressure$pressure, geom="line")
ggplot(pressure, aes(x=temperature, y=pressure)) + geom_line() # 同上
qplot(temperature, pressure, data=pressure, geom="point")
ggplot(pressure, aes(x=temperature, y=pressure)) + geom_point() # 同上
qplot(temperature, pressure, data=pressure, geom=c("line", "point"))
ggplot(pressure, aes(x=temperature, y=pressure)) + geom_line() + geom_point() # 同上
qplot(temperature, pressure, data=pressure, geom="bar", stat="identity") # 这里的identity表示按照y值来确定条形的高度
ggplto(pressure, aes(x=temperature, y=pressure)) + geom_bar() # 同上
qplot(temperature, pressure, data=pressure, geom="boxplot")
f <- function(x) {2*pi*x}
qplot(c(-3, 3), fun=f, stat="function", geom="line")
ggplot(BOD, aes(x=Time, y=demand)) + geom_bar(stat="identity", fill="lightblue", colour="black") # fill表示填充颜色；colour表示边框颜色
```

# 簇状条形图与频数条形图
```sh
library(gcookbook)
ggplot(cabbage_exp, aes(x=Date, y=Weight, fill=Cultivar)) + geom_bar(position="dodge", stat="identity")
ggplot(diamonds, aes(x=cut)) + geom_bar(stat=bin) # bin表示频数
```

# 条形图重新着色
```r
library(gcookbook)
upc <- subset(uspopchange, rand(Change)>40)
ggplot(upc, aes(x=Abb, y=Change, fill=Region)) + geom_bar(stat="identity")
ggplot(upc, aes(x=reorder(Abb, Change), y=Change, fill=Region)) + geom_bar(stat="identity", colour="black") + scale_fill_manual(values=c("#669933", "#FFCC66")) + xlab("State")
csub <- subset(climate, Source=="Berkeley" & Year>1900) # 分正负着色
csub$pos <- csub$Anomaly10y>=0
ggplot(csub, aes(x=Year, y=Anomaly10y, fill=pos)) + geom_bar(stat="identity", position="identity")
```

# 绘制点线图
```r
tophit <- tophitters2001[1:25, ]
ggplot(tophit, aes(x=reorder(name, avg), y=avg)) + geom_point(size=3) + theme_bw() + theme(axis.text.x=element_text(angle=60, hjust=1), panel.grid.major.y=element_blank(), panel.grid.major.x=element_line(colour="grey60", linetype="dashed"))
ggplot(tophit, aes(x=avg, y=name)) + geom_segment(aes(yend=name), xend=0, colour="grey50", size=1.5) + geom_point(size=3, aes(colour=lg)) + scale_colour_brewer(palette="Set1", limits=c("NL", "AL")) + theme_bw() + theme(panel.grid.major.y=element_blank(), legend.position=c(1, 0.55), legend.justification=c(1, 0.5))
ggplot(tophit, aes(x=avg, y=name)) + geom_segment(aes(yend=name), xend=0, colour="grey50", size=1.5) + geom_point(size=3, aes(colour=lg)) + scale_colour_brewer(palette="Set1", limits=c("NL", "AL"), guide=FALSE) + theme_bw() + theme(panel.grid.major.y=element_blank()) + facet_grid(lg ~ ., scales="free_y", space="free_y")
ggplot(BOD, aes(x=Time, y=demand, group=1)) + geom_line() + ylim(0, max(BOD$demand))
tg <- data.frame(supp=c("OJ","OJ","OJ","VC","VC","VC"), dose=c(0.5,1.0,2.0,0.5,1.0,2.0), length=c(13.23,22.70,26.06,7.98,16.77,26.14))
ggplot(tg, aes(x=dose, y=length, color=factor(supp))) + geom_line()
ggplot(tg, aes(x=dose, y=length, linetype=factor(supp))) + geom_line()
ggplot(tg, aes(x=dose, y=length, shape=factor(supp))) + geom_line() + geom_point(size=4)
ggplot(tg, aes(x=dose, y=length, fill=factor(supp))) + geom_line() + geom_point(size=4, shape=21)
ggplot(tg, aes(x=dose, y=length, colour=factor(supp), group=factor(supp))) + geom_line(linetype="dashed", size=1, colour="lightblue") + geom_point(shape=22, size=3, fill="white")
sunspotyear <- data.frame(Year=as.numeric(time(sunspot.year)), Sunspots=as.numeric(sunspot.year))
ggplot(sunspotyear, aes(x=Year, y=Sunspots)) + geom_area(colour="black", fill="blue", alpha=.2)
ggplot(uspopage, aes(x=Year, y=Thousands, fill=AgeGroup, order=desc(AgeGroup))) + geom_area() + scale_fill_brewer(palette="Blues")
clim <- subset(climate, Source=="Berkeley", select=c("Year", "Anomaly10y", "Unc10y"))
ggplot(clim, aes(x=Year, y=Anomaly10y)) + geom_ribbon(aes(ymin=Anomaly10y-Unc10y, ymax=Anomaly10y+Unc10y), alpha=0.2) + geom_line() # alpha表示透明度
ggplot(heightweight, aes(x=ageYear, y=heightIn)) + geom_point() + stat_smooth(method=lm, colour="red", level=0.99) # 添加回归模型拟合线并设置置信域为99%
ggplot(heightweight, aes(x=ageYear, y=heightIn)) + geom_point() + stat_smooth(method=lm, se=FALSE) # 无置信域
ggplot(heightweight, aes(x=ageYear, y=heightIn, colour=sex)) + geom_point() + stat_smooth(method=lm, se=FALSE, fullrange=TRUE)
ts <- subset(countries, Year==2009&healthexp>2000)
ggplot(ts, aes(x=healthexp, y=infmortality)) + geom_point() + annotate("text", x=4350, y=5.4, label="Canada") + annotate("text", x=7400, y=6.8, label="USA")
ggplot(ts, aes(x=healthexp, y=infmortality)) + geom_point() + geom_text(aes(label=Name, y=infmortality+0.1), size=4, vjust=0)
ggplot(faithful, aes(x=waiting)) + geom_histogram(binwidth=5, fill="white", colour="black")
ggplot(birthwt, aes(x=bwt, fill=factor(smoke))) + geom_density(alpha=.3)
birthwt1 <- birthwt
birthwt1$smoke <- revalue(birthwt1$smoke, c("0"="No Smoke", "1"="Smoke"))
ggplot(birthwt1, aes(x=bwt)) + geom_density() + facet_grid(smoke ~ .)
ggplot(faithful, aes(x=eruptions, y=waiting)) + geom_point() + stat_density2d()
ggplot(faithful, aes(x=eruptions, y=waiting)) + stat_density2d(aes(fill=..density..), geom="raster", contour=FALSE)
ggplot(subset(climate, Source=="Berkeley"), aes(x=Year, y=Anomaly10y)) + geom_line() + annotate("rect", xmin=1950, xmax=1980, ymin=-1, ymax=1, alpha=.1, fill="blue")
ggplot(diamonds, aes(x=cut)) + geom_bar() + theme(axis.text.x = element_text(family="Times", face="italic", colour="blue", size=rel(0.9))) # 修改坐标字体
ggplot(wind, aes(x=DirCat, fill=SpeedCat)) + geom_histogram(binwidth=15, origin=-7.5) + coord_polar() + scale_x_continuous(limits=c(0,360
ggplot(diamonds, aes(x=cut)) + geom_bar() + ggtitle("Diamonds Cut") + theme(plot.title=element_text(family="Times", face="bold.italic", colour="red"), axis.title.x=element_text(size=13, colour="blue"))
library(RColorBrewer)
display.brewer.all()
ggplot(uspopage, aes(x=Year, y=Thousands, fill=AgeGroup)) + geom_area() + scale_fill_brewer(palette="Greys")
install.packages("corrplot")
library(corrplot)
mcor <- cor(mtcars)
corrplot(mcor)
corrplot(mcor, method="shade", shade.col=NA, tl.col="black", tl.srt=45, addCoef.col="black")
ggplot(data.frame(x=c(-3,3)), aes(x=x)) + stat_function(fun=dnorm)
dnorm_limit <- function(x) {
	y <- dnorm(x)
	y[x < 0 | x > 2] <- NA
	return y
}
ggplot(data.frame(x=c(-3,3)), aes(x=x)) + stat_function(fun=dnorm_limit, geom="area", fill="blue", alpha=.2) + stat_function(fun=dnorm)
```
