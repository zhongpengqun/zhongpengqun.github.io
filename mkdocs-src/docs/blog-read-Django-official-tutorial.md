- http://www.djangoproject.com/

Django is a high-level Python web framework that encourages rapid development and clean, `pragmatic` design.
Built by `experienced developers`, it takes care of much of the `hassle` of web development

`Ridiculously` fast

`Reassuringly` secure
令人放心的

`Exceedingly` scalable

Stay in the loop
随时了解情况

`Sharpen your skills`

The DSF awards prizes to recognize the contributions of volunteers in the Django community.
以表彰Django社区志愿者的贡献

Get in touch
取得联系

Corporate Members
公司成员

Individual members `are appointed to` the Django Software Foundation `in recognition of` their contributions to the Django community
Django软件基金会任命了个别成员，以表彰他们对Django社区的贡献

If you `know of` someone that you think should be a member, including yourself, please `fill out this form`

`From scratch`: Overview | Installation

How the documentation is organized

take you by the hand through a series of steps to create a web application
带您手动完成创建web应用程序的一系列步骤

How-to guides are `recipes`. They `guide you` through `the steps involved` in `addressing key problems` and use-cases. They are more advanced than tutorials and `assume` some knowledge of how Django works.
	- recipe

They call that `callable` to `invoke` the database query, and they can do what they want around that `cal`

Django provides an abstraction layer (the “models”) for structuring and `manipulating` the data of your web application
	- manipulate & handle
		- Manipulate 显示出技巧性和处理问题的艺术性，例如一件工具或仪器

Django has the concept of “views” to `encapsulate` the `logic responsible` for processing a user’s request and for returning the response

Forms
Django provides a rich framework to `facilitate` the creation of forms and the manipulation of form data
	- manipulate data

Security is a topic of `paramount` importance in the development of web applications

- Design philosophies (复数形式)
	- Loose coupling
		- A fundamental goal of Django’s stack is `loose coupling and tight cohesion`
		- Although Django `comes with` a full stack `for convenience`, the `pieces of the stack` are `independent of another` wherever possible.
	- Less code
		- Django apps should use `as little code as possible`; they should lack `boilerplate`(样板文件). Django should `take full advantage of` Python’s `dynamic capabilities`, such as `introspection`
	- Quick development
		- The point of a web framework in the 21st century is to make the `tedious（乏味的） aspects of` web development fast

	- Don’t repeat yourself (DRY)
		- The framework, within reason, should deduce as much as possible from as little as possible
		在合理的范围内，框架应该从尽可能少的东西中推断出尽可能多的东西

	- Explicit is better than implicit
		- This is a core Python principle listed in PEP 20, and it means Django shouldn’t do too much “magic.” Magic shouldn’t happen `unless` there’s a really good reason for it. `Magic is worth using only if it creates a huge convenience unattainable in other ways`, and it isn’t implemented in a way that confuses developers who are trying to learn how to use the feature
	- Models
		- Explicit is better than implicit
			- Fields shouldn’t assume certain behaviors based solely（仅仅） on the name of the field. This requires too much knowledge of the system and is prone to errors（容易出错）. Instead, behaviors should be based on keyword arguments and, in some cases, on the type of the field
				- 在某些情况下
					- in some cases
				- solely
					- adv 唯一地;仅;只;唯;单独地
					- solely VS merely

the `outer` directory, its name doesn't matter to Djanog
	- the `inner` directory


This feature is meant as a shortcut, not as `definitive` model generation.
