#coding=utf-8
import sys
import os
import random
import time

class Game(object):
	
	def __init__(self):	
		self.Pk_me = 2		#自己的战斗力
		self.Pk_start_room = 5	#大胡子的战斗力
		self.Pk_hospital_room = 6   #医生的战斗力
		self.Pk_boss_room = 10  #监狱长的战斗力
		self.Game_items = []	#物品栏
		self.Game_box = 0	#是否打开了小木盒
		self.Game_cook_room = 0	#是否拿了钥匙
		self.Game_hospital_room = 0 #是否拿到解药
		self.Game_poisoned = 1 #是否中毒
		self.Game_start_room = 0  #是否得到逃跑路线
		self.dama_doctor = 0 #是否给了医生大麻
		self.Game_boss_room = 0  #boss的攻略程度
	
	def cmd_clear(self):		#清屏
		i = os.system('cls')
	
	def word_split(self):
		print "-------------------------------------------------------------------------------"
		
	def choose_print(self):	#选择提示
		choose = raw_input("\n你决定>".decode('utf-8').encode('gbk'))
		return choose
	
	def game_items_print(self):	#显示物品栏
		print u"\n物品："
		x = 1
		for i in self.Game_items:	
			print str(x) + "、".decode('utf-8').encode('gbk') + i.decode('utf-8').encode('gbk')
			x += 1
		print u""
		return x
		
	def game_items_check(self): #详细查看物品栏
		self.word_split()
		items_count = self.game_items_print()
		print u"（输入物品编号查看详细介绍）"
		self.word_split()
		
		if len(self.Game_items):
		
			while True:
				choose = self.choose_print()
				try:
					i = int(choose)
					i = i - 1
					break
				except:
					print u"\n无效的输入"
			if i >= items_count - 1 or i < 0: 	
				print u"\n无效的输入"
				raw_input()
				self.go_room()
			else:		
				if self.Game_items[i] and self.Game_items[i] == "大麻":
					print u"\n吸一口可以让人嗨起来！"
					raw_input()
					self.go_room()
				elif self.Game_items[i] and self.Game_items[i] == "一叠毛爷爷":
					print u"\n有钱能使磨推鬼！"
					raw_input()
					self.go_room()
				elif self.Game_items[i] and self.Game_items[i] == "钥匙":
					print u"\n一把亮闪闪的钥匙！"
					raw_input()
					self.go_room()
				elif self.Game_items[i] and self.Game_items[i] == "大力丸":
					print u'\n一颗黑色的小药丸，上面刻着"大力出奇迹"！\n'
					self.word_split()
					print u'(1)吃下去    (2)再等等'
					
					while True:
						choose = self.choose_print()
						if choose == "1":
							print u"\n你感觉到身体里充满了力量！"
							self.Game_items.remove("大力丸")
							self.Pk_me = 8
							raw_input()
							self.go_room()
						elif choose == "2":
							print u"\n你想了想，没有吃下去。"
							raw_input()
							self.go_room()
						else:
							print u"\n别犯傻，你不能那样做..."
				elif self.Game_items[i] and self.Game_items[i] == "葵花宝典":
					print u'\n翻开第一页：欲练此功，挥刀自宫。\n'
					self.word_split()
					print u'(1)无所谓了，挥刀自宫！     (2)什么鬼，不练！'
					
					while True:
						choose = self.choose_print()
						if choose == "1":
							print u"\n啊...你感觉到身体里有一种无敌的力量！\n"
							print u"你翻到最后一页：若不自宫，也可成功！\n"
							print u"......"
							self.Game_items.remove("葵花宝典")
							self.Pk_me = 10
							raw_input()
							self.go_room()
						elif choose == "2":
							print u"\n你合上了书。"
							raw_input()
							self.go_room()
						else:
							print u"\n别犯傻，你不能那样做..."
				elif self.Game_items[i] and self.Game_items[i] == "装满液体的小瓶":
					print u'\n一个玻璃小瓶，里面装着天蓝色的液体\n'
					self.word_split()
					print u'(1)喝下去！     (2)再等等'
					
					while True:
						choose = self.choose_print()
						if choose == "1":
							print u"\n你感觉到身体暖洋洋的，就是肚子有点不舒服...\n"
							print u"上完厕所你感觉一阵轻松。\n"
							self.Game_items.remove("装满液体的小瓶")
							self.Game_poisoned = 0
							raw_input()
							self.go_room()
						elif choose == "2":
							print u"\n你想了想，没有喝下去。"
							raw_input()
							self.go_room()
						else:
							print u"\n别犯傻，你不能那样做..."
				elif self.Game_items[i] and self.Game_items[i] == "入狱档案":
					print u"""\n入狱档案：

姓名： 高富帅

背景：毛里求斯国王私生子

入狱原因：太高、太富、太帅！
											
你：......WTF,这是我？还是不知道的好！
															
					"""
					raw_input()
					self.go_room()
				elif self.Game_items[i] and self.Game_items[i] == "实验资料":
					print u"""\n实验资料：

甲方：xx公司

乙方：xxx监狱
					
化工原料三聚氰胺的临床实验
					
xxxxxxxxxxxxxxxxxxxxxxxxxx
					
结论：吃不死人......
															
					"""
					raw_input()
					self.go_room()
				else:
					pass
					
					
		else:
			print u"没有任何物品"
			raw_input()
			self.go_room()
		
	def box(self):	#小木盒
		if self.Game_box == 0:
			self.Game_items.append("一叠毛爷爷")
			self.word_split()
			print u"\n打开小木盒，「得到一叠毛爷爷」\n"
			self.word_split()
			self.Game_box = 1	
		else: 
			self.word_split()
			print u"\n里面是空的...\n"
			self.word_split()
		
	def pk(self, me, him):	#pk
		if me >= him:
			self.word_split()
			print  u"\n太牛了，你轻松的打扁了对方！"
		else:
			self.cmd_clear()
			self.word_split()
			print u"\n你死了...鲁迅说：有的人死了，他还活着。\n"
			self.word_split()
			raw_input()
			print u"(1)重新开始    (2)退出游戏"
			
			while True:
				choose = self.choose_print()
				if choose == "1":
					self.play()
				elif choose == "2":
					exit()
				else:
					print u"\n别犯傻，你不能那样做..."
					
	def Russian_Roulette(self):		#俄罗斯轮盘
		i = random.randint(1, 6)
		self.cmd_clear()
		self.word_split()
		print u"(1)朝自己开枪！    (2)你来！"
		x = 1	#打到第几颗子弹
		y = 0 	#boss是否开过枪
		while True:
			print u"\n第%d轮" % x
			choose = self.choose_print()
			if choose == "1":
				if x != i:
					print u"\n你朝自己的脑袋上开了一枪！"
					print u"\n枪没响，你躲过一劫！"
					x += 1
					y = 0
				else:
					print u"\n砰，你倒在血泊之中...运气太差了！\n"
					self.word_split()
					raw_input()
					print u"(1)重新开始    (2)退出游戏"
			
					while True:
						choose = self.choose_print()
						if choose == "1":
							self.play()
						elif choose == "2":
							exit()
						else:
							print u"\n别犯傻，你不能那样做..."		
							
			elif choose == "2" and y == 0:
				if x != i:
					print u"\n监狱长朝自己的脑袋上开了一枪！"
					print u"\n枪没响，你的死亡率又上升了！"
					x += 1
					y = 1
				else:
					print u"\n砰，监狱长倒在血泊之中！你活下来了！"
					print u'\n(死了...说好的真实身份哪？还是我自己来找吧。)'
					print u"\n「你得到入狱档案」\n"
					self.word_split()
					self.Game_items.append("入狱档案")
					self.Game_boss_room = 2
					raw_input()
					self.go_room()
			elif choose == "2" and y == 1:
				print u'\n监狱长："我已经开过枪了，该你了！"'
			else:
				print u"\n别犯傻，你不能那样做..."
		
		
		
	def play(self):  #开始游戏
		self.__init__()
		self.game_start()
	
	def end(self):	#结局
		if self.Game_poisoned == 1 and self.Game_boss_room == 0:
			self.cmd_clear()
			self.word_split()
			print u"\n你在晚上神不知鬼不觉的溜出了监狱\n"
			print u"在外面的世界，你也不停的找寻自己身份的消息，但却一无所获。\n"
			print u"渐渐的，你总是会突然的昏倒，在一次昏倒后你再也没能醒来...\n"
			print "bad end 1\n"
			self.word_split()
			raw_input()
			print u"(1)重新开始    (2)退出游戏"
			
			while True:
				choose = self.choose_print()
				if choose == "1":
					self.play()
				elif choose == "2":
					exit()
				else:
					print u"\n别犯傻，你不能那样做..."
			
		elif self.Game_poisoned == 0 and self.Game_boss_room == 0:
			self.cmd_clear()
			self.word_split()
			print u"\n你在晚上神不知鬼不觉的溜出了监狱\n"
			print u"在外面的世界，你也不停的找寻自己身份的消息，但却一无所获。\n"
			print u"因为越狱所以被警察全国通缉，你只能东躲西藏度日。\n"
			print "bad end 2\n"
			self.word_split()
			raw_input()
			print u"(1)重新开始    (2)退出游戏"
			
			while True:
				choose = self.choose_print()
				if choose == "1":
					self.play()
				elif choose == "2":
					exit()
				else:
					print u"\n别犯傻，你不能那样做..."
					
		elif self.Game_poisoned == 1 and self.Game_boss_room == 1:
			self.cmd_clear()
			self.word_split()
			print u"\n你在晚上神不知鬼不觉的溜出了监狱\n"
			print u"你公开了监狱长的秘密，却并没有人愿意相信。\n"
			print u"在外面的世界，你也不停的找寻自己身份的消息，但却一无所获。\n"
			print u"渐渐的，你总是会突然的昏倒，在一次昏倒后你再也没能醒来...\n"
			print "bad end 3\n"
			self.word_split()
			raw_input()
			print u"(1)重新开始    (2)退出游戏"
			
			while True:
				choose = self.choose_print()
				if choose == "1":
					self.play()
				elif choose == "2":
					exit()
				else:
					print u"\n别犯傻，你不能那样做..."
					
		elif self.Game_poisoned == 1 and self.Game_boss_room == 2:
			self.cmd_clear()
			self.word_split()
			print u"\n你在晚上神不知鬼不觉的溜出了监狱\n"
			print u"你公开了监狱长的秘密，却并没有人愿意相信。\n"
			print u"渐渐的，你总是会突然的昏倒，在一次昏倒后你再也没能醒来...\n"
			print "bad end 4\n"
			self.word_split()
			raw_input()
			print u"(1)重新开始    (2)退出游戏"
			
			while True:
				choose = self.choose_print()
				if choose == "1":
					self.play()
				elif choose == "2":
					exit()
				else:
					print u"\n别犯傻，你不能那样做..."
					
		elif self.Game_poisoned == 0 and self.Game_boss_room == 1:
			self.cmd_clear()
			self.word_split()
			print u"\n你在晚上神不知鬼不觉的溜出了监狱\n"
			print u"你公开了监狱长的秘密，却并没有人愿意相信。\n"
			print u"因为越狱所以被警察全国通缉，你只能东躲西藏度日。\n"
			print "bad end 5\n"
			self.word_split()
			raw_input()
			print u"(1)重新开始    (2)退出游戏"
			
			while True:
				choose = self.choose_print()
				if choose == "1":
					self.play()
				elif choose == "2":
					exit()
				else:
					print u"\n别犯傻，你不能那样做..."
					
		elif self.Game_poisoned == 0 and self.Game_boss_room == 2:
			self.cmd_clear()
			self.word_split()
			print u"\n你在晚上神不知鬼不觉的溜出了监狱\n"
			print u"你公开了监狱长的秘密，一切真相大白，监狱长的同伙受到了法律的严惩！\n"
			print u"因表彰你的功绩，所以法院准许你提前出狱。\n"
			print "good end\n"
			self.word_split()
			raw_input()
			print u"(1)重新开始    (2)退出游戏"
			
			while True:
				choose = self.choose_print()
				if choose == "1":
					self.play()
				elif choose == "2":
					exit()
				else:
					print u"\n别犯傻，你不能那样做..."
		else:
			pass
		
	def print_slow(self, word): #慢速输出
		for i in word:
			sys.stdout.write(i)
			sys.stdout.flush()
			time.sleep(0.05)
	
	def go_room(self): 	#选择进入房间
		self.cmd_clear()
		self.word_split()
		print u"(1)去双人监狱    (2)去监狱食堂    (3)去监狱操场\n\n(4)去监狱医疗室    (5)去监狱长的办公室    (6)查看物品栏"
		while True:
			choose = self.choose_print()
				
			if choose == "1":
				self.start_room()
			elif choose == "2":
				self.cook_room()
			elif choose == "3":
				self.playground_room()
			elif choose == "4":
				self.hospital_room()
			elif choose == "5":
				self.boss_room()	
			elif choose == "6":
				self.game_items_check()
			else:
				print u"\n别犯傻，你不能那样做..."
	
	def game_start(self):	#游戏开始
		self.cmd_clear()
		self.print_slow(u"\n滴、滴、滴。。。好像是时钟走动的声音。\n\n")
		self.print_slow(u"你慢慢的睁开了眼睛。\n\n")
		self.print_slow(u'"这是哪里？" "我是谁？" "我好像什么都不记得了..."')
		raw_input()
		self.start_room()
	
	def start_room(self): #开始的房间
		self.cmd_clear()
		self.word_split()
		print u"\n这是一间上下铺的双人监狱，对面的墙上贴着一张大大的好莱坞美女海报。\n"
		print u"你从下铺的床上起来，活动了下有点僵硬的四肢。\n"
		print u"上铺坐着的是一个满脸大胡子穿着监狱制服的男人，看起来一副不好惹的样子。\n"
		print u"你的床上放着一个小木盒，仿佛在召唤着你打开它。\n"
		self.word_split()
		print u"(1)和大胡子狱友对话    (2)打开小木盒    (3)离开这里"
		
		while True:
			choose = self.choose_print()
			
			if choose == "1" and self.Game_start_room == 0:
				self.cmd_clear()
				self.word_split()
				print u'\n你拍了下狱友的肩膀：“伙计，这是哪里？我是...谁？”\n'
				print u'"你脑子烧坏了？？"\n'
				print u'"要是再给我装X，我就把桌脚塞到你的脑袋里面!!"他恶臭的口水喷了你一脸。\n'
				self.word_split()
				print u"(1)哈哈，开个玩笑    (2)投其所好    (3)今天让哥教你怎么做人    (4)返回"
				
				while True:
					choose = self.choose_print()
				
					if choose == "1":
						self.cmd_clear()
						self.word_split()
						print u'\n“哈哈哈...这一点也不好笑!!”\n'
						self.word_split()
						print u"(1)哈哈，开个玩笑    (2)投其所好    (3)今天让哥教你怎么做人    (4)返回"
					elif choose == "2":
						self.cmd_clear()
						self.word_split()
						if "大麻" in self.Game_items:
							self.Game_items.remove("大麻")
							print u'\n「你失去了一份大麻」\n'
							print u'你："兄弟，我这里有好东西...一起抽两口？"\n'
							print u'狱友："哥们上道啊，告诉你一个秘密，墙上的海报后面有一个通向外面下水道的洞！"\n'
							print u'狱友："是我用藏在《圣经》里的小锤子，一点点挖了好几年。"\n'
							print u'狱友："不过下水道的门需要钥匙才能打开"\n'
							print u'狱友："钥匙本来已经弄到手了，有一次在食堂吃饭的时候弄丢了..."\n'
							self.word_split()
							print u"(1)和大胡子狱友对话    (2)打开小木盒    (3)离开这里"
							self.Game_start_room = 1
							break
						else:	
							print u'\n你：“兄弟，我这里有好东西...”\n'
							print u'狱友：“什么东西，我怎么没看见。”\n'
							self.word_split()
							print u"(1)和大胡子狱友对话    (2)打开小木盒    (3)离开这里"
							break	
					elif choose == "3":
						self.cmd_clear()
						self.word_split()
						print u'\n"你扑了上去，和他扭打在了一起。"\n'
						self.word_split()
						raw_input()
						self.pk(self.Pk_me, self.Pk_start_room)
						print u'\n狱友："别再打我英俊的脸，告诉你一个秘密，墙上的海报后面有一个通向外面下水道的洞！"\n'
						print u'狱友："是我用藏在《圣经》里的小锤子，一点点挖了好几年。"\n'
						print u'狱友："不过下水道的门需要钥匙才能打开"\n'
						print u'狱友："钥匙本来已经弄到手了，有一次在食堂吃饭的时候弄丢了..."\n'
						self.word_split()
						self.Game_start_room = 1
						print u"(1)和大胡子狱友对话    (2)打开小木盒    (3)离开这里 "
						break
					elif choose == "4":
						self.cmd_clear()
						self.word_split()
						print u"(1)和大胡子狱友对话    (2)打开小木盒    (3)离开这里 "
						break
					else:
						print u"\n别犯傻，你不能那样做..."
			elif choose == "1" and self.Game_start_room == 1:
				self.cmd_clear()
				self.word_split()
				print u'\n"找到钥匙就可以逃跑了！到时候别忘记带上我！"\n'
				self.word_split()
				print u"(1)逃出监狱    (2)返回"
				while True:
					choose = self.choose_print()
				
					if choose == "1" and "钥匙" in self.Game_items:
						self.end()
					elif choose == "1" and "钥匙" not in self.Game_items:
						self.cmd_clear()
						self.word_split()
						print u"\n你爬入海报后面的洞里，到下水道的时候被一扇铁门挡住了，需要一把钥匙。\n"
						self.word_split()
						print u"(1)和大胡子狱友对话    (2)打开小木盒    (3)离开这里"
						break
					elif choose == "2":
						self.cmd_clear()
						self.word_split()
						print u"(1)和大胡子狱友对话    (2)打开小木盒    (3)离开这里"
						break
					else:
						print u"\n别犯傻，你不能那样做..."
			
			elif choose == "2":
				self.cmd_clear()
				self.box()
				print u"(1)和大胡子狱友对话    (2)打开小木盒    (3)离开这里"
			elif choose =="3":
				self.go_room()
			else:
				print u"\n别犯傻，你不能那样做..."
				
	def cook_room(self): 	#监狱食堂
		self.cmd_clear()
		self.word_split()
		print u"\n你来到了监狱食堂，这里和一般公司的食堂差不了多少，只是充斥着一股刺鼻的汗臭味\n"
		self.word_split()
		print u"(1)四处看看    (2)离开这里"
		
		while True:
			choose = self.choose_print()
			
			if choose == "1":
				self.cmd_clear()
				self.word_split()
				print u"\n有些人紧缩着眉头，默默吃着饭。\n"
				print u"有几个人疯疯癫癫，自言自语着什么东西。\n"
				print u"一个男人在饭桌上用手指画着什么东西，你觉得他好像有点眼熟。\n"
				self.word_split()
				print u"(1)和他对话    (2)返回"
				while True:
					choose = self.choose_print()
			
					if choose == "1":
						self.cmd_clear()
						self.word_split()
						print u'\n"上次那个问题你想好答案了吗？"\n'
						print u'你说："什么问题？我不记得了。"\n'
						print u'"我再说一遍，世界上最好的编程语言是什么？"\n'
						self.word_split()
						choose = self.choose_print()
						
						if choose == "php" and self.Game_cook_room == 0:
							self.cmd_clear()
							self.word_split()
							print u'\n"咦，你也是同行啊！哈哈哈。"\n'
							print u'"这把钥匙是我在这里捡到的，就送给你了。"\n'
							print u'「得到钥匙」\n'
							self.word_split()
							self.Game_items.append("钥匙")
							print u"(1)四处看看    (2)离开这里"
							self.Game_cook_room = 1
							break
						elif choose == "php" and self.Game_cook_room == 1:
							self.cmd_clear()
							self.word_split()
							print u'\n"咦，你也是同行啊！哈哈哈。"\n'
							self.word_split()
							print u"(1)四处看看    (2)离开这里"
							break
						else:
							self.cmd_clear()
							self.word_split()
							print u'\n"你还真是无趣啊..."\n'
							self.word_split()
							print u"(1)四处看看    (2)离开这里"
							break
					elif choose == "2":
						self.cmd_clear()
						self.word_split()
						print u"(1)四处看看    (2)离开这里"
						break
					else:
						print u"\n别犯傻，你不能那样做..."
					
			elif choose == "2":
				self.go_room()
			else:
				print u"\n别犯傻，你不能那样做..."
				
	def playground_room(self): 	#监狱操场
		self.cmd_clear()
		self.word_split()
		print u"\n猛烈的阳光照射在监狱操场上，热气仿佛把眼前的景色都扭曲了。\n"
		print u"操场上散布着三三两两的囚犯，贪婪的沐浴着难得一见的阳光。\n"
		print u"一个蓬头垢面的男人盯着你边点头边笑。\n"
		self.word_split()
		print u"(1)和他对话    (2)离开这里"
		while True:
			choose = self.choose_print()
			if choose == "1":
				self.cmd_clear()
				self.word_split()
				print u'\n"呵呵呵，少年我看你骨骼惊奇，日后必是可造之材。"\n'
				print u'"我这里有各种仙丹秘籍，你来看看。"\n'
				print u'"我的东西，连医生都喜欢来点。嘿嘿。"\n'
				self.word_split()
				print u"(1)两份大麻    (2)大力丸    (3)葵花宝典"
				while True:
					choose = self.choose_print()
					if "一叠毛爷爷" in self.Game_items and choose == "1":
						self.cmd_clear()
						self.word_split()
						print u"\n「你失去了一叠毛爷爷」"
						print u"\n「你得到两份大麻」\n"
						self.Game_items.remove("一叠毛爷爷")
						self.Game_items.append("大麻")
						self.Game_items.append("大麻")
						self.word_split()
						print u"(1)和他对话    (2)离开这里"
						break
					elif "一叠毛爷爷" in self.Game_items and choose == "2":
						self.cmd_clear()
						self.word_split()
						print u"\n「你失去了一叠毛爷爷」"
						print u"\n「你得到大力丸」\n"
						self.Game_items.remove("一叠毛爷爷")
						self.Game_items.append("大力丸")
						self.word_split()
						print u"(1)和他对话    (2)离开这里"
						break
					elif "一叠毛爷爷" in self.Game_items and choose == "3":
						self.cmd_clear()
						self.word_split()
						print u"\n「你失去了一叠毛爷爷」"
						print u"\n「你得到葵花宝典」\n"
						self.Game_items.remove("一叠毛爷爷")
						self.Game_items.append("葵花宝典")
						self.word_split()
						print u"(1)和他对话    (2)离开这里"
						break
					elif "一叠毛爷爷" in self.Game_items:
						print u"\n少年，你再好好选选。\n"
					else:
						self.cmd_clear()
						self.word_split()
						print u"\n没钱你装个P啊，老子白笑了。滚！\n"
						self.word_split()
						print u"(1)和他对话    (2)离开这里"
						break
			elif choose == "2":
				self.go_room()
			else:
				print u"\n别犯傻，你不能那样做..."
			
	def hospital_room(self): 	#监狱医疗室
		self.cmd_clear()
		self.word_split()
		print u"\n刚进医疗室，阴森的感觉扑面而来，每一根汗毛都竖立起来。\n"
		print u"旁边的柜子上放着一个难看的硕大鱼缸，里面却没有一条鱼。"
		print u"\n白色的桌子前坐着一个戴眼镜的中年男子，看样子是这里的医生。\n"
		self.word_split()
		print u"(1)和他对话    (2)四处看看    (3)离开这里"
		
		while True:
			choose = self.choose_print()
			
			if choose == "1" and self.Game_hospital_room == 0:
				self.cmd_clear()
				self.word_split()
				print u'\n"医生，我最近感觉失去了一些记忆，想不起以前的事了。"\n'
				print u'医生："噢，是吗？看来剂量有点大..."\n'
				print u'"什么剂量？？"\n'
				print u'医生："啊，我是说上次给你开的头痛药...休息几天就没事了。"\n'
				print u'(这医生好像在隐瞒着什么)\n'
				self.word_split()
				print u"(1)投其所好    (2)用拳头让他说实话    (3)返回"
				
				while True:
					choose = self.choose_print()
			
					if choose == "1":
						self.cmd_clear()
						self.word_split()
						if "大麻" in self.Game_items and self.dama_doctor == 0:
							self.Game_items.remove("大麻")
							print u'\n「你失去了一份大麻」'
							print u'\n"医生，我这里有点好东西...要不要来两口。"\n'
							print u'"这怎么好意思...以后要开药，尽管来找我!"\n'
							print u'"你随便坐一下，我要找个好地方来过过瘾。"\n'
							print u"趁医生出去的时候，你搜索了医疗室。\n"
							print u"「你得到一个装满液体的小瓶」\n"
							self.word_split()
							self.Game_items.append("装满液体的小瓶")
							self.dama_doctor = 1
							print u"(1)和他对话    (2)四处看看    (3)离开这里"
							break
						elif self.dama_doctor == 1:
							print u"\n谢谢不用了，这玩意不能搞太多。\n"
							self.word_split()
							print u"(1)和他对话    (2)四处看看    (3)离开这里"
							break
						elif "大麻" not in self.Game_items:
							print u'\n"医生，我这里有点好东西..."\n'
							print u'医生:"你误会了，我不搞基。"\n'
							print u'......\n'
							self.word_split()
							print u"(1)和他对话    (2)四处看看    (3)离开这里"
							break
						else:
							pass
					elif choose == "2":
						self.cmd_clear()
						self.word_split()
						print u'\n"我要用拳头让你明白撒谎的代价！"\n'
						print u'医生:"我要用枪让你明白，谁才是老大！"\n'
						self.word_split()
						raw_input()
						self.pk(self.Pk_me, self.Pk_hospital_room)
						print u"\n你用迅雷不及掩耳的速度夺取了医生的手枪。\n"
						print u'医生:"大哥！别开枪，是自己人啊！"\n'
						print u'医生:"监狱长是主谋，我也是受害者。"\n'
						print u'"把你知道的都说出来！"\n'
						print u'医生:"我只知道监狱长在犯人身上做一些化学药品的人体实验。"\n'
						print u'医生:"我只是帮他记录实验犯人的身体情况而已。"\n'
						print u'你把枪口对准医生"对我做了什么药品实验？解药在哪里？"\n'
						print u'医生:"别开枪，有的，有的！解药在这里！"\n'
						print u"「你得到一个装满液体的小瓶」\n"
						self.word_split()
						self.Game_items.append("装满液体的小瓶")
						self.Game_hospital_room = 1
						print u"(1)和他对话    (2)四处看看    (3)离开这里"
						break
					elif choose == "3":
						self.cmd_clear()
						self.word_split()
						print u"(1)和他对话    (2)四处看看    (3)离开这里"
						break
					else:
						print u"\n别犯傻，你不能那样做..."
			elif choose == "1" and self.Game_hospital_room == 1:
				self.cmd_clear()
				self.word_split()
				print u'\n医生："我知道的都告诉你啦，别的事情除了监狱长没人知道。"\n'
				self.word_split()
				print u"(1)和他对话    (2)四处看看    (3)离开这里"
			elif choose == "2":
				self.cmd_clear()
				self.word_split()
				print u"\n随意的看了下四周，桌子上有个亮闪闪的物体。\n"
				print u"你仔细一看，发现桌子的角落里有一颗子弹壳。\n"
				self.word_split()
				print u"(1)和他对话    (2)四处看看    (3)离开这里"
			elif choose == "3":
				self.go_room()
			else:
				print u"\n别犯傻，你不能那样做..."
	
	def boss_room(self):
		if self.Game_boss_room == 0:
			self.cmd_clear()
			self.word_split()
			print u"\n咚、咚、咚 你敲开了监狱长的办公室"
			print u"\n红木桌子前坐着一个肥胖的中年男子，看来是这里的监狱长。\n"
			print u'监狱长："找我有什么事？"\n'
			self.word_split()
		elif self.Game_boss_room == 1:
			self.cmd_clear()
			self.word_split()
			print u'\n监狱长："你敢不敢跟我赌一吧，赢了我就告诉你真实身份，输了就把资料还给我。"\n'
			self.word_split()
		elif self.Game_boss_room == 2:
			self.cmd_clear()
			self.word_split()
			print u'\n监狱长倒在一片血泊中...\n'
			self.word_split()
		else:
			pass
			
		if self.Game_hospital_room == 0 and self.Game_boss_room == 0:
			print u"(1)我最近失去了一些记忆    (2)没什么事"
		
			while True:
				choose = self.choose_print()
				self.cmd_clear()
				self.word_split()
				
				if choose == "1":
					print u'\n监狱长："狱中生活比较辛苦单调，这种事情很常见。"\n'
					print u'监狱长："没有其他事的话，你就快点走吧。"\n'
					self.word_split()
					raw_input()
					self.go_room()
				elif choose == "2":
					print u'\n监狱长："没有事不要乱进我的办公室！"\n'
					print u'监狱长："快滚！空气都快被你弄脏了！"\n'
					self.word_split()
					raw_input()
					self.go_room()
				else:
					print u"\n别犯傻，你不能那样做..."
					
		elif self.Game_hospital_room == 1 and self.Game_boss_room == 0:
			print u"(1)我已经知道你干的好事了，狗日的！    (2)没什么事"
		
			while True:
				choose = self.choose_print()
				self.cmd_clear()
				self.word_split()
				if choose == "1":
					print u'\n"医生把你的恶行都告诉我了！竟然把我们当成实验品！"'
					print u'\n监狱长："这贱人，又泄露我的秘密，看来也是留不得！"'
					print u'\n监狱长："哼哼，是又如何！"'
					print u'\n你："吃我一招！"'
					print u'\n监狱长："嘿嘿！你以为我做到这个位置靠的是什么？"\n'
					self.word_split()
					raw_input()
					self.pk(self.Pk_me, self.Pk_boss_room)
					print u'\n监狱长："不可能，你怎么这么强？"'
					print u'\n你："那当然。日出东方，唯我不败！"'
					print u'\n监狱长："什么？？"'
					print u'\n你："咳咳...不要在意这些细节。快把你的罪证交出来！"'
					print u'\n监狱长："输了就是输了，给你吧。"'
					print u'\n「得到一份实验资料」'
					print u'\n监狱长："等等！你敢不敢跟我赌一吧，赢了我就告诉你真实身份，输了就把资料还给我。"'
					self.word_split()
					print u'(1)有什么不敢，来赌！    (2)走了，我都赢了还玩个P！'
					self.Game_items.append("实验资料")
					self.Game_boss_room = 1
					
					while True:
						choose = self.choose_print()
						
						if choose == "1":
							self.cmd_clear()
							self.word_split()
							print u'\n"怎么个赌法？"'
							print u'\n监狱长:"很简单，俄罗斯轮盘！"'
							print u'\n说明:俄罗斯轮盘是一种自杀式玩命游戏。参与者在左轮手枪的弹巢放入一颗或多颗子弹'
							print u'\n之后将子弹盘旋转，然后关上。参与者轮流把手枪对着自己的头，按下扳机；直至有人中'
							print u'\n枪，或不敢按下扳机为止。传说这种“游戏”源自十九世纪俄罗斯，由监狱的狱卒强迫囚'
							print u'\n犯进行，以作为赌博。亦有说这是源自决斗的方法。也有说是亡命之徒之间用作比拼勇气。\n'
							self.word_split()
							raw_input()
							self.Russian_Roulette()
						elif choose == "2":
							self.go_room()
						else:
							print u"\n别犯傻，你不能那样做..."
							
				elif choose == "2":
					print u'\n监狱长："没有事不要乱进我的办公室！"\n'
					print u'监狱长："快滚！空气都快被你弄脏了！"\n'
					self.word_split()
					raw_input()
					self.go_room()
				else:
					print u"\n别犯傻，你不能那样做..."	
					
		elif self.Game_hospital_room == 1 and self.Game_boss_room == 1:	
			print u'(1)有什么不敢，来赌！    (2)走了，我都赢了还玩个P！'
			while True:
				choose = self.choose_print()
						
				if choose == "1":
					self.cmd_clear()
					self.word_split()
					print u'\n"怎么个赌法？"'
					print u'\n监狱长:"很简单，俄罗斯轮盘！"'
					print u'\n说明:俄罗斯轮盘是一种自杀式玩命游戏。参与者在左轮手枪的弹巢放入一颗或多颗子弹'
					print u'\n之后将子弹盘旋转，然后关上。参与者轮流把手枪对着自己的头，按下扳机；直至有人中'
					print u'\n枪，或不敢按下扳机为止。传说这种“游戏”源自十九世纪俄罗斯，由监狱的狱卒强迫囚'
					print u'\n犯进行，以作为赌博。亦有说这是源自决斗的方法。也有说是亡命之徒之间用作比拼勇气。\n'
					self.word_split()
					raw_input()
					self.Russian_Roulette()
					self.Game_boss_room = 2
				elif choose == "2":
					self.go_room()
				else:
					print u"\n别犯傻，你不能那样做..."
		elif self.Game_hospital_room == 1 and self.Game_boss_room == 2:	
			print u'(1)离开这里!'
			while True:
				choose = self.choose_print()
						
				if choose == "1":
					self.go_room()
				else:
					print u"\n别犯傻，你不能那样做..."
		else:
			pass
		
a_game = Game()
a_game.play()			