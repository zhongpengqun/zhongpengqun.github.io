# coding: utf-8
import re

en = """In receiving the distinction with which your free Academy has so generously honoured me, my gratitude has been profound, particularly when I consider the extent to which this recompense has surpassed my personal merits. Every man, and for stronger reasons, every artist, wants to be recognized. So do I. But I have not been able to learn of your decision without comparing its repercussions to what I really am. A man almost young, rich only in his doubts and with his work still in progress, accustomed to living in the solitude of work or in the retreats of friendship: how would he not feel a kind of panic at hearing the decree that transports him all of a sudden, alone and reduced to himself, to the centre of a glaring light? And with what feelings could he accept this honour at a time when other writers in Europe, among them the very greatest, are condemned to silence, and even at a time when the country of his birth is going through unending misery?

I felt that shock and inner turmoil. In order to regain peace I have had, in short, to come to terms with a too generous fortune. And since I cannot live up to it by merely resting on my achievement, I have found nothing to support me but what has supported me through all my life, even in the most contrary circumstances: the idea that I have of my art and of the role of the writer. Let me only tell you, in a spirit of gratitude and friendship, as simply as I can, what this idea is.

For myself, I cannot live without my art. But I have never placed it above everything. If, on the other hand, I need it, it is because it cannot be separated from my fellow men, and it allows me to live, such as I am, on one level with them. It is a means of stirring the greatest number of people by offering them a privileged picture of common joys and sufferings. It obliges the artist not to keep himself apart; it subjects him to the most humble and the most universal truth. And often he who has chosen the fate of the artist because he felt himself to be different soon realizes that he can maintain neither his art nor his difference unless he admits that he is like the others. The artist forges himself to the others, midway between the beauty he cannot do without and the community he cannot tear himself away from. That is why true artists scorn nothing: they are obliged to understand rather than to judge. And if they have to take sides in this world, they can perhaps side only with that society in which, according to Nietzsche’s great words, not the judge but the creator will rule, whether he be a worker or an intellectual.

By the same token, the writer’s role is not free from difficult duties. By definition he cannot put himself today in the service of those who make history; he is at the service of those who suffer it. Otherwise, he will be alone and deprived of his art. Not all the armies of tyranny with their millions of men will free him from his isolation, even and particularly if he falls into step with them. But the silence of an unknown prisoner, abandoned to humiliations at the other end of the world, is enough to draw the writer out of his exile, at least whenever, in the midst of the privileges of freedom, he manages not to forget that silence, and to transmit it in order to make it resound by means of his art.

None of us is great enough for such a task. But in all circumstances of life, in obscurity or temporary fame, cast in the irons of tyranny or for a time free to express himself, the writer can win the heart of a living community that will justify him, on the one condition that he will accept to the limit of his abilities the two tasks that constitute the greatness of his craft: the service of truth and the service of liberty. Because his task is to unite the greatest possible number of people, his art must not compromise with lies and servitude which, wherever they rule, breed solitude. Whatever our personal weaknesses may be, the nobility of our craft will always be rooted in two commitments, difficult to maintain: the refusal to lie about what one knows and the resistance to oppression.

For more than twenty years of an insane history, hopelessly lost like all the men of my generation in the convulsions of time, I have been supported by one thing: by the hidden feeling that to write today was an honour because this activity was a commitment – and a commitment not only to write. Specifically, in view of my powers and my state of being, it was a commitment to bear, together with all those who were living through the same history, the misery and the hope we shared. These men, who were born at the beginning of the First World War, who were twenty when Hitler came to power and the first revolutionary trials were beginning, who were then confronted as a completion of their education with the Spanish Civil War, the Second World War, the world of concentration camps, a Europe of torture and prisons – these men must today rear their sons and create their works in a world threatened by nuclear destruction. Nobody, I think, can ask them to be optimists. And I even think that we should understand – without ceasing to fight it – the error of those who in an excess of despair have asserted their right to dishonour and have rushed into the nihilism of the era. But the fact remains that most of us, in my country and in Europe, have refused this nihilism and have engaged upon a quest for legitimacy. They have had to forge for themselves an art of living in times of catastrophe in order to be born a second time and to fight openly against the instinct of death at work in our history.

Each generation doubtless feels called upon to reform the world. Mine knows that it will not reform it, but its task is perhaps even greater. It consists in preventing the world from destroying itself. Heir to a corrupt history, in which are mingled fallen revolutions, technology gone mad, dead gods, and worn-out ideologies, where mediocre powers can destroy all yet no longer know how to convince, where intelligence has debased itself to become the servant of hatred and oppression, this generation starting from its own negations has had to re-establish, both within and without, a little of that which constitutes the dignity of life and death. In a world threatened by disintegration, in which our grand inquisitors run the risk of establishing forever the kingdom of death, it knows that it should, in an insane race against the clock, restore among the nations a peace that is not servitude, reconcile anew labour and culture, and remake with all men the Ark of the Covenant. It is not certain that this generation will ever be able to accomplish this immense task, but already it is rising everywhere in the world to the double challenge of truth and liberty and, if necessary, knows how to die for it without hate. Wherever it is found, it deserves to be saluted and encouraged, particularly where it is sacrificing itself. In any event, certain of your complete approval, it is to this generation that I should like to pass on the honour that you have just given me.

At the same time, after having outlined the nobility of the writer’s craft, I should have put him in his proper place. He has no other claims but those which he shares with his comrades in arms: vulnerable but obstinate, unjust but impassioned for justice, doing his work without shame or pride in view of everybody, not ceasing to be divided between sorrow and beauty, and devoted finally to drawing from his double existence the creations that he obstinately tries to erect in the destructive movement of history. Who after all this can expect from him complete solutions and high morals? Truth is mysterious, elusive, always to be conquered. Liberty is dangerous, as hard to live with as it is elating. We must march toward these two goals, painfully but resolutely, certain in advance of our failings on so long a road. What writer would from now on in good conscience dare set himself up as a preacher of virtue? For myself, I must state once more that I am not of this kind. I have never been able to renounce the light, the pleasure of being, and the freedom in which I grew up. But although this nostalgia explains many of my errors and my faults, it has doubtless helped me toward a better understanding of my craft. It is helping me still to support unquestioningly all those silent men who sustain the life made for them in the world only through memory of the return of brief and free happiness.

Thus reduced to what I really am, to my limits and debts as well as to my difficult creed, I feel freer, in concluding, to comment upon the extent and the generosity of the honour you have just bestowed upon me, freer also to tell you that I would receive it as an homage rendered to all those who, sharing in the same fight, have not received any privilege, but have on the contrary known misery and persecution. It remains for me to thank you from the bottom of my heart and to make before you publicly, as a personal sign of my gratitude, the same and ancient promise of faithfulness which every true artist repeats to himself in silence every day."""



cn = """尊敬的国王和皇后陛下，尊敬的王室成员，女士们，先生们：

秉承自由精神的贵学院慷慨授予我这份殊荣，我自认我的成就远远配不上它的分量，所以更是由衷地心怀感激。

所有人都渴望得到认可，艺术家就更为如此。我也是一样。只有当我将你们的决定所产生的影响与真实的我进行比较之后，我才真正理解你们何以作了这样一个决定。

一个尚且年轻的人，除了疑惑一无所有，他的作品尚未成型，并且习惯于在工作中孤独地生活，对各种示好也退避三舍，对于这样一个离群索居的人来说，突然被逮到，并抛置于这耀眼的聚光灯下，又怎么能不感到一种恐慌呢？

当欧洲其他的作家，哪怕是其中最伟大的一些作家，都被迫保持沉默，当他的故土，正遭受着无止境的苦难，他将以怎样的心情来接受这份荣誉呢？

我就经历了这种内心的惶恐与不安。

为了重新获得平静，我只能接受这份命运慷慨的馈赠。既然我的成就无法与这份奖项匹配，我便只能倚赖那份支撑着我人生的信念，即便在最艰难的境况下也未曾抛却我的那份信念：那就是我对我的艺术以及对作家这一角色的看法。

让我怀着感激和友好的心情，对大家尽可能简短地表达一下这个想法。

于我而言，没有艺术，我便无法存活。但我从没有把这份艺术置于一切之上，相反，它之所以对我而言不可或缺，正是因为它与所有人紧紧相连，并且允许像我这样的一个人能和大家一样生活下去。

艺术在我看来并不是一场孤独的狂欢。艺术是一种手段，它以其特有的方式呈现了人类共同的苦难与欢乐，从而感动了大多数的人。

所以它迫使艺术家不再自我孤立，使其屈从于一种最为质朴、最为普世的真理。

而通常情况下，那个自认与众不同而选择艺术生涯的人很快就会发现，只有承认自己与众生的共性，他的艺术和他的独特才能从中得到滋养。

正是在这种自身与他者不断的往来中、在与他不可搁置的美以及不可抽离的群体的交往之中，艺术家得到了自我锤炼。

这也是为什么真正的艺术家不会蔑视任何东西；他们要求自己必须理解一切，而不是评判一切。

如果他们必须在这个世界上选择一个阵营，那他们或许只能属于尼采的伟大言论中所构建的那种社会：一个由创造者而不是评判者来统治的社会，无论这里的创造者是劳动人民还是知识分子。

同样地，作家这一角色也被赋予了艰难的职责。

身为作家，在如今这个年代，他不该为制造历史的人服务，他应该为承受历史的人服务。 否则，他将被孤立，也将失去他的艺术。

一个作家，若是与独裁者为伍，那么即便独裁者有千军万马与之同行，他也依然无法摆脱那种孤独。

但世界另一头，一个被遗弃在屈辱中的无名之囚，他的沉默却足以一次又一次将作家从这种孤独的流放中拯救出来，

只要他在享有自由权利的同时，始终不忘这种沉默，并以艺术的方式来使这种沉默发出声响。

我们中任何人都没有伟大到足以承担这一使命。

但是在他一生的境遇中，无论是门庭冷落还是扬名一时，无论是被压制于暴政的桎梏之下还是拥有一时的言论自由，

作家只有忠心耿耿竭尽所能地为真理和自由服务，他的职业才能因此变得伟大，他才能得到民众发自肺腑的正名。

作家的使命，就是团结尽可能多的人，这个使命不应屈服于谎言和奴役，因为在谎言和奴役统治的土地上，处处囚禁着孤独的灵魂。

无论我们作为个人有着怎样的弱点，我们职业的高贵却永远扎根在两个并不容易坚守的承诺里：对于知晓的事，绝无谎言；对于任何压迫，反抗到底。

在二十多年的荒诞历程中，孤立无援的我和同代人一样，迷失在时代的跌宕变迁中， 仅靠内心隐隐的一种感觉支撑着：在当今这个世界，写作是一种光荣，因为这一行为肩负使命，并迫使你不仅仅去写作。

它尤其迫使我按我自己的方式，以我的一己之力，与所有和我一样经历过那段历史的人一起去承担起我们共有的那种痛苦与希冀。

这些人，出生于第一次世界大战之初；希特勒政权建立和最初的革命浪潮掀起时，他们又正值二十多岁。

接着，像是要使他们的经历更加完整，他们又经历了西班牙内战、第二次世界大战，

他们经历了那个满目疮痍、遍地集中营和牢狱的欧洲，而如今，正是他们这些人，又要在毁灭性核武器的威胁下，抚育他们的下一代，完成他们的使命。

我想，没有任何人有权利要求他们乐观。

我甚至主张，在与他们不断斗争的同时，我们应该理解他们的所作所为：他们只是因为与日俱增的绝望，而做出了耻辱之举，并且堕入了这个时代所盛行的虚无主义。

但是，不论是在我们国家，还是在整个欧洲，我们中的大多数，仍然拒绝虚无主义，仍在寻找一种正义。

我们需要锻造一种在多事之秋生活的艺术，为的是能够涅槃重生，然后坦然地与那历史进程中的死亡本能作斗争。

或许，每代人都自信肩负着重塑世界的使命。然而，我们这代人却知道，我们对此无能为力。

但是，我们这代人的使命或许更伟大，因为我们的使命是：不让这个世界分崩离析。

我们继承的，是一段残破的历史，它混杂着革命的失败、走火入魔的科技、已经死去的诸神和穷途末路的意识形态，纵使在这样的时代，任何平庸的势力都能让这个世界毁于一旦，

但这种平庸的势力只有否定的力量，在理智自甘堕落成仇恨与压迫的奴隶时，这种否定的力量并不能教会我们这代人在内心和外部世界重新修建起一点点能够给予生命和死亡以尊严的东西。

在这样一个每时每刻都有可能崩塌的世界面前，我们伟大的裁判官们建立的恐怕永远是死亡的国度，

而我们这代人知道，我们应该在与时间疯狂赛跑的同时，在不同民族之间，建立起一种不屈从于任何奴役的和平，重新调和工作与文化的关系，并与全世界所有人携起手来，构建一种联盟。

没有人能够确定我们这代人是否能完成这项浩大的任务，但是，我们确定的是，他们已经遍布在全世界各个角落，为真理和自由而战，并时刻准备着为之赴死，无怨无悔。

正是这些人，值得我们尊敬和鼓励，无论在何时何地——尤其是在他们牺牲的地方。总之，我想把你们刚刚授予我的荣耀转献给他们，相信你们也会感同身受。

与此同时，在说了作家职业的高尚之后，我想要还原作家的真实模样，除了和他的战友们一起共享的身份之外，他没有其他身份。

他既脆弱又固执；他无法永远保持公正，却又热切追寻着公正；

在所有人的视线中，他默默构建着自己的作品，既不以之为耻，也不引以为傲，他永无止息地在痛苦与美好中被撕扯，

最终是为了从他这双重的存在中，提炼出他固执地想要在历史的废墟中创建起来的东西。

这么说完，谁还能期待他给出现成的答案和完美的道德信条呢？

真理是神秘的、难以捕捉的，总是有待征服的。

自由固然是令人振奋的，但实践起来也同样是危险的、艰难的。

我们必须走向这两个目标，艰苦卓绝、征途漫漫，却坚定不移、矢志不渝。

由此，哪个有着自知之明的作家还敢自诩为美德的传道者？

至于我，我必须再说一次，这完全不是我的身份。

我从来未能放弃生命中的光和幸福，不能放弃自由的生活，这些东西自小就伴随着我成长。

这种怀旧之情虽然也让我犯了不少错误，却无疑也帮助我更好地理解了我的职业，

帮助我毫不犹豫地站在那些沉默的人身边，那些人，除了从回忆中追索那一点点短暂而自由的幸福，在这个世上便无以为继。

现在，我向大家还原了真实的我，你们知道了我的浅薄有限，知道了我得益于他人，也知道了我艰难的信仰，

作为结束，我终于能更自如地表达诸位授予我这份荣誉的广博与慷慨，也能更自如地对你们说，

我接受这份荣誉，并要把它视作为一种致敬，向所有和我一样经历了战斗，却没有获得任何殊荣，只是饱经了苦难与迫害的人致敬。

最后，我要发自肺腑地对诸位表示感谢，并公开地，以感恩的心，向你们作出一个古老的承诺，

任何一个真正的艺术家每天都会在静默中向自己作出的古老的承诺，那便是——忠诚。"""


# xx = re.findall('[a-zA-Z]+\([\u4e00-\u9fff]+\)__[a-zA-Z|\u4e00-\u9fff]+__', ss)
# result = {}
# for x in xx:
#     result.update({re.findall('[a-zA-Z]+', x)[0]: x})
# for k, v in result.items():
#     to_be_handle = to_be_handle.replace(k, v)
# print(to_be_handle)


cn = """福柯和布朗肖见过一次吗？对于福柯来说，答案是否定的。对于布朗肖来说，答案则是肯定的。1968年五月风暴期间，福柯和布朗肖在索邦大学的校园内相遇了。在那个风起云涌的日子里，陌生人之间的讨论并不突兀。布朗肖认出了已经大名鼎鼎的福柯，并和他讲过几句话。但是，福柯并不知道同他讲话的这个人就是他的偶像布朗肖。尽管布朗肖名声显赫，但二战以后几乎从未抛头露面。他只通过写作的方式在场。除了他的著作，人们对他一无所知。只是在五月风暴期间，他才唯一一次以匿名者的身份出现在公开场合。福柯当然不会认出他来。布朗肖不接受记者采访，不暴露自己的照片，也不参加学术会议，甚至也极少同自己的朋友（包括最好的朋友列维纳斯）见面，他和朋友的交往方式就是不间断地写信。他过着隐居而隔绝的生活，就像他一再在他的书中所表达的那样，他赋予了沉默、孤独和距离以独特的价值。不和人面对面说话，布朗肖就采取尼采的方式，自己和自己热烈地谈话，一个孤独者和他的影子在说话。他常常在书中自问自答，自己和自己进行“无限的交谈”。到2003年他去世之前，人们并不清楚，这个被称为法国二十世纪最著名的失踪者，到底是否还在人世。

在六十年代，福柯读过布朗肖的大量著作。布朗肖成为福柯最迷恋的作者之一。福柯在各种不同的场合多次毫不掩饰地表达对布朗肖的敬意。他曾对他的朋友说，他年轻的时候，梦想成为布朗肖。他在文中大量引用布朗肖的话，仿照布朗肖的风格，他在《知识考古学》后面所采用的自问自答的方式就是对布朗肖的模仿和致敬。布朗肖、巴塔耶和克罗索夫斯基，这三个人同时是哲学家和作家，他们也是福柯五六十年代迷恋的三个作者。正是他们决定性地把福柯引向了尼采。“对我来说，尼采、巴塔耶、布朗肖、克罗索夫斯基是逃离哲学的途径。巴塔耶的狂暴，布朗肖既诱人又恼人的甜蜜，克罗索夫斯基的螺旋，这些都是从哲学出发，把哲学带入游戏和疑问，从哲学中出来，再回到哲学中去。”他们都打破了哲学和非哲学的界线——这也正是福柯的风格。不过，他和他们并不来往。他只是在罗兰·巴特的引荐下同克罗索夫斯基见面并建议了牢靠的友谊。而巴塔耶1962年就过早地去世，隐居者布朗肖则从不见人。对福柯来说，他也愿意保持着对布朗肖的神秘崇拜。或许，保持距离，正是他们之间的内在默契。有一次，一个朋友邀请福柯同布朗肖共进晚餐，被福柯婉言谢绝了：只通过读他的文章来认识他和理解他。两人刻意地不见面。但是，用布朗肖的说法，他们“都惦念着对方”。

福柯是通过萨特的文章发现布朗肖的，但是，他很快就站在布朗肖的一边来反对萨特。如果说，萨特是六十年代法国思想界的太阳，而隐匿的布朗肖则是思想界的暗夜。但神秘的布朗肖是如何发现福柯的？经过一个出版界朋友的推荐，布朗肖看到了福柯尚未出版的博士论文《古典时代疯狂史》的手稿，就对这个默默无闻的年轻人大为赞赏。在本书出版后，布朗肖最早为这本书写了热情洋溢的评论文章。福柯1984年去世之后，布朗肖写了《我想象中的米歇尔·福柯》，对福柯的所有重要著作，对他的整个学术生涯作了全面的评价——显然，他在持续地阅读和关注福柯。为什么是想象中的米歇尔·福柯？就是因为从未谋面。这是一种从未见面的保持距离的友谊。何谓保持距离的友谊？布朗肖在他出版的《友谊》一书中作了这样的解释：

我们必须以一种陌生人的关系迎接他们，他们也以这种关系迎接我们，我们之间相互形同路人。友谊，这种没有依靠、没有故事情节的关系，然而所有生命的朴实都进入其中，这种友谊以通过对共同未知的承认的方式进行，因此它不允许我们谈论我们的朋友，我们只能与他们对话，不能把他们作为我们谈话（文章）的话题，即使在理解活动之中，他们对我们言说也始终维持一种无限的距离，哪怕关系再为要好，这种距离是一种根本的分离，在这个基础上，那分离遂成为一种联系。这种分离不是拒绝交谈知心话语（这是多么俗气，哪怕只是想想），而就是存在于我和那个称为朋友的人之间的这种距离，一种纯净的距离，衡量着我们之间的关系，这种阻隔让我永远不会有权力去利用他，或者是利用我对他的认识（即便是去赞扬他），然而，这并不会阻止交流，而是在这种差异之中，有时是在语言的沉默中我们走到了一起。

这是布朗肖独特的友谊观。自亚里士多德以来，友谊总是同分享和共存联系起来。友谊就是要共同生活（罗兰·巴特曾经在法兰西学院的一年课程中专门讨论过这个问题：如何共同生活？）。如果长时间不来往，友谊就渐趋熄灭。友谊正是在共享中得以持久和维护：共同享受美好的时光，共同享受彼此之间的快乐和福音，正是在这种分享中，友谊得以深化。而蒙田还不满足于共享这个概念。对他来说，真正的友谊不仅是分享和相互理解，而是两个人灵魂的完全交流，真正的朋友其内心深处是一模一样的，两个灵魂复合在一起毫无差异。此刻，朋友之间不存在所谓的感激、义务和责任。因为好的朋友就如同一个人，一个人不过是另外一个人的影像，他们之间达成了彻底的重叠，也就是说，完全没有距离。蒙田说：“我这里要说的友谊，则是两颗心灵叠合，我中有你，你中有我，浑然成为一体，令二者联结起来的纽带已消隐其中，再也无从辨认。”因此，“他们间所有的一切，包括意志、思想、观点、财产、妻子、儿女、荣誉和生命，都是共同拥有的。他们行动一致，依据亚里士多德的定义，他们是一个灵魂占据两个躯体，所以他们之间不能给予或得到任何东西。”

我们看到，布朗肖是对这种漫长而根深蒂固的友谊观念的一个拒绝，他扭转了友谊讨论的方向：友谊不是无限地接近。相反，友谊就是不见面，就是保持距离，就是对距离和差异的刻意维护，就是朋友之间的沉默以对。或许，正是因为有这种差异和沉默，友谊才会更加纯净，朋友之间的友谊纽带不会成为羁绊，或者说，朋友之间不存在纽带，“分离遂成为一种联系”。

而福柯对沉默和友谊的关系也有一种特殊的感受，在一次访谈中，他说：

某些沉默带有强烈的敌意，另一些沉默却意味着深切的友谊、崇敬，甚至爱情。我深深地记得制片人丹尼尔·施密特造访我时的情景，我们才聊了几分钟，就不知怎地突然发现彼此间没有什么可说的了。接下来我们从下午三点钟一直待到午夜。我们喝酒，猛烈地抽烟，还吃了丰盛的晚餐。在整整十小时中，我们说的话不超过二十分钟。从那时起，我们之间开始了漫长的友谊。这是我第一次在沉默中同别人发生友情。

或许，在布朗肖和福柯之间发生的就是这类友谊：不见面，保持纯净的距离，没有世俗的任何污染，从而让朋友处在绝对的自由状态。与此同时，以写作和阅读的方式，关注对方，评论对方，和对方彼此交流。这种友谊不存在“私交”。这就是布朗肖所说的“知识友谊”。但是，这种友谊从不轻易地说出来，这种友谊需要以沉默的方式来维护，对这种友谊的言说和宣称，不是对它的肯定，而是对它的损耗。朋友，只有在朋友永远地离开的时候，只有朋友永远听不到朋友这个称呼的时候，才可以被宣称。也正是在福柯永远无法倾听的时候，布朗肖才开始公开地宣示这种友谊：是的，福柯是他的朋友。“友谊是许诺在身后赠给福柯的礼物。它超越于强烈情感之外，超越于思索问题之外，超越于生命危险之外……我坚信，不管处境多么尴尬，我仍然忠实于这一份知识友谊。福柯的逝世令我悲痛不已，但它却允许我今天向他宣示这份友谊。”

尽管福柯不能向布朗肖宣称这种友谊了——两个朋友，总有一个人要先走的，总有一个人不能向另外一个人公开地宣示友谊——但是，我们仍旧可以想象福柯会认同布朗肖的做法。因为，在罗兰·巴特逝世后，福柯在他的追悼致辞中所表达的对友谊的看法，同布朗肖所说的具有惊人的相似性。也是在巴特去世后，福柯才宣示这种友谊。福柯说，罗兰·巴特“二十多年不懈的努力获得了社会的公认，并具有独创性的重要研究成果，这使我无需借助我与他的友谊……请允许我在今天下午披露这唯一的友谊。这种友谊与它所痛恨的死亡至少在寡言少语上是相似的”。同样，友谊只能在死后披露；友谊只发生在沉默寡言之中；友谊不是任何务实的工具。这不就是布朗肖对逝去的福柯所说的吗？

布朗肖在他的这篇纪念文章的最后引用了亚里士多德的名言：“朋友啊，世上是没有朋友的。”通常，这是一个令人奇怪的矛盾修辞：怎么能称呼一个人为朋友，怎么能对着一个朋友的面，但同时又对他说世上根本就没有朋友呢？但是，在布朗肖这里，这句话完全没有任何的悖论：是的，世上已经没有福柯这个朋友了。所以，现在，我可以称他为我的朋友。这是“没有私交”的朋友，沉默的朋友，是纯粹的“知识友谊”。"""



cn = cn.replace('\n', '')
en = en.replace('\n', '')

cns = cn.split('。')
ens = en.split('.')

for x in range(52):
    print(ens[x])
    print('\n')
    print(cns[x])
    print('\n')
    print('<hr>')
