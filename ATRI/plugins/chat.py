import os
import nonebot
import random
from pathlib import Path
from random import randint, choice
from datetime import datetime
from nonebot import CommandSession
from nonebot import on_command


bot = nonebot.get_bot()


@nonebot.scheduler.scheduled_job(
    'cron',
    day_of_week = "mon,tue,wed,thu,fri,sat,sun",
    hour = 7
)
async def _():
    '''早安'''
    try:
        group_list = await bot.get_group_list() #type: ignore
        groups = [group['group_id'] for group in group_list]
        res = randint(1,2)
        if res == 1:
            msg = random.choice(
                [
                    '啊......早上好...(哈欠)',
                    '唔......吧唧...早上...哈啊啊~~~\n早上好......',
                    '早上好......',
                    '早上好呜......呼啊啊~~~~',
                    '啊......早上好。\n昨晚也很激情呢！',
                    '吧唧吧唧......怎么了...已经早上了么...',
                    '早上好！',
                    '......看起来像是傍晚，其实已经早上了吗？',
                    '早上好......欸~~~脸好近呢'
                    '......(打瞌睡)',
                ]
            )
        
        elif res == 2:
            img = Path('.') / 'ATRI' / 'data' / 'voice' / 'SY.jpg'
            msg = f'[CQ:image,file=file:///{os.path.abspath(img)}]'

        for group in groups:
            await bot.send_group_msg(group_id = group, message = msg) #type: ignore
    
    except:
        pass


@nonebot.scheduler.scheduled_job(
    'cron',
    day_of_week = "mon,tue,wed,thu,fri,sat,sun",
    hour = 22
)
async def _():
    '''晚安'''
    try:
        group_list = await bot.get_group_list() #type: ignore
        groups = [group['group_id'] for group in group_list]
        res = randint(1,2)
        if res == 1:
            msg = random.choice(
                [
                    '忙累了一天，快休息吧',
                    '辛苦了一天，准备睡觉吧',
                    '一起睡觉吧~~~~~',
                    '......该睡觉了',
                    '还不睡等着猝死？嗯！？'

                ]
            )

        elif res == 2:
            img = choice(
                [
                    'SJ.jpg', 'SJ1.jpg'
                ]
            )
            img = Path('.') / 'ATRI' / 'data' / 'voice' / f'{img}'
            msg = f'[CQ:image,file=file:///{os.path.abspath(img)}]'

        for group in groups:
            await bot.send_group_msg(group_id = group, message = msg) #type: ignore

    except:
        pass


def now_time():
    now_ = datetime.now()
    hour = now_.hour
    minute = now_.minute
    now = hour + minute / 60
    return now


@on_command('morning', patterns = [r"早[安哇]|早上好|ohayo|哦哈哟|お早う"], only_to_me = False)
async def az(session: CommandSession):
    if 5.5 <= now_time() < 9:
        await session.send(
            choice(
                [
                    '啊......早上好...(哈欠)',
                    '唔......吧唧...早上...哈啊啊~~~\n早上好......',
                    '早上好......',
                    '早上好呜......呼啊啊~~~~',
                    '啊......早上好。\n昨晚也很激情呢！',
                    '吧唧吧唧......怎么了...已经早上了么...',
                    '早上好！',
                    '......看起来像是傍晚，其实已经早上了吗？',
                    '早上好......欸~~~脸好近呢'
                ]
            )
        )
    
    elif 9 <= now_time() < 18:
        await session.send(
            choice(
                [
                    '哼！这个点还早啥，昨晚干啥去了！？',
                    '熬夜了对吧熬夜了对吧熬夜了对吧？？？！',
                    '是不是熬夜是不是熬夜是不是熬夜？！'
                ]
            )
        )
    
    elif 18 <= now_time() < 24:
        await session.send(
            choice(
                [
                    '早个啥？哼唧！我都准备洗洗睡了！',
                    '不是...你看看几点了，哼！',
                    '晚上好哇'
                ]
            )
        )
    
    elif 0 <= now_time() < 5.5:
        await session.send(
            choice(
                [
                    'zzzz......',
                    'zzzzzzzz......',
                    'zzz...好涩哦..zzz....',
                    '别...不要..zzz..那..zzz..',
                    '嘻嘻..zzz..呐~..zzzz..',
                    '...zzz....哧溜哧溜....'
                ]
            )
        )

@on_command('noon', patterns = [r"中午好|午安"], only_to_me = False)
async def _(session: CommandSession):
    if 11 <= now_time() <= 15:
        await session.send(
            choice(
                [
                    '午安w','午觉要好好睡哦，ATRI会陪伴在你身旁的w',
                    '嗯哼哼~睡吧，就像平常一样安眠吧~o(≧▽≦)o',
                    '睡你午觉去！哼唧！！'
                ]
            )
        )


@on_command('night', patterns = [r"晚安|oyasuminasai|おやすみなさい"], only_to_me = False)
async def az(session: CommandSession):
    if 5.5 <= now_time() < 11:
        await session.send(
            choice(
                [
                    '你可猝死算了吧！',
                    '？啊这',
                    '亲，这边建议赶快去睡觉呢~~~',
                    '不可忍不可忍不可忍！！为何这还不猝死！！'
                ]
            )
        )
    
    elif 11 <= now_time() < 15:
        await session.send(
            choice(
                [
                    '午安w','午觉要好好睡哦，ATRI会陪伴在你身旁的w',
                    '嗯哼哼~睡吧，就像平常一样安眠吧~o(≧▽≦)o',
                    '睡你午觉去！哼唧！！'
                ]
            )
        )
    
    elif 15 <= now_time() < 19:
        await session.send(
            choice(
                [
                    '难不成？？晚上不想睡觉？？现在休息',
                    '就......挺离谱的...现在睡觉',
                    '现在还是白天哦，睡觉还太早了'
                ]
            )
        )
    
    elif 19 <= now_time() < 24:
        await session.send(
            choice(
                [
                    '嗯哼哼~睡吧，就像平常一样安眠吧~o(≧▽≦)o',
                    '......(打瞌睡)',
                    '呼...呼...已经睡着了哦~...呼......',
                    '......我、我会在这守着你的，请务必好好睡着'
                ]
            )
        )
    
    elif 0 <= now_time() < 5.5:
        await session.send(
            choice(
                [
                    'zzzz......',
                    'zzzzzzzz......',
                    'zzz...好涩哦..zzz....',
                    '别...不要..zzz..那..zzz..',
                    '嘻嘻..zzz..呐~..zzzz..'
                ]
            )
        )


@on_command('az', patterns = [r"[aA][zZ]|[阿啊]这"], only_to_me = False)
async def az(session: CommandSession):
    res = randint(1,3)
    if res == 1:
        # res = random.randint(1,10)
        img = choice(
            [
                'AZ.jpg', 'AZ1.jpg', 'AZ2.jpg', 'AZ3.png', 'ZN.jpg'
            ]
        )
        img = Path('.') / 'ATRI' / 'data' / 'emoji' / f'{img}'
        img = os.path.abspath(img)
        await session.send(f'[CQ:image,file=file:///{img}]')

@on_command('suki', patterns = [r"喜欢|爱你|爱|suki|daisuki|すき|好き|贴贴|老婆|[Mm][Uu][Aa]|亲一个"], only_to_me = True)
async def az(session: CommandSession):
    res = randint(1,3)
    if res == 1:
        # res = random.randint(1,10)
        img = choice(
            [
                'SUKI.jpg', 'SUKI1.jpg', 'HE1.jpg'
            ]
        )
        img = Path('.') / 'ATRI' / 'data' / 'emoji' / f'{img}'
        img = os.path.abspath(img)
        await session.send(f'[CQ:image,file=file:///{img}]')
    
    elif 2 <= res <= 3:
        img = choice(
            [
                'TZ.jpg', 'TZ1.jpg', 'TZ1.jpg'
            ]
        )
        img = Path('.') / 'ATRI' / 'data' / 'emoji' / f'{img}'
        img = os.path.abspath(img)
        await session.send(f'[CQ:image,file=file:///{img}]')


@on_command('wenhao', patterns = [r"'?'|？"], only_to_me = False)
async def az(session: CommandSession):
    res = randint(1,3)
    if res == 1:
        res = randint(1,5)
        if 1 <= res < 2:
            await session.send(
                choice(
                    [
                        '?', '？', '嗯？', '(。´・ω・)ん?', 'ん？'
                    ]
                )
            )
        
        elif 2 <= res <= 5:
            img = choice(
                [
                    'WH.jpg', 'WH1.jpg', 'WH2.jpg', 'WH3.jpg', 'WH4.jpg'
                ]
            )
            img = Path('.') / 'ATRI' / 'data' / 'emoji' / f'{img}'
            img = os.path.abspath(img)
            await session.send(f'[CQ:image,file=file:///{img}]')

@on_command('yn', patterns = [r"是[吗]|是否"], only_to_me = False)
async def az(session: CommandSession):
    if randint(1,3) == 1:
        img = choice(
            [
                'YIQI_YES.png', 'YIQI_NO.jpg', 'KD.jpg', 'FD.jpg'
            ]
        )
        img = Path('.') / 'ATRI' / 'data' / 'emoji' / f'{img}'
        img = os.path.abspath(img)
        await session.send(f'[CQ:image,file=file:///{img}]')



@on_command('kouchou', patterns = [r"草你妈|操|你妈|脑瘫|废柴|fw|five|废物|战斗|爬|爪巴|sb|SB|啥[b批比逼]|傻b|2b"], only_to_me = False)
async def az(session: CommandSession):
    if randint(1,2) == 1:
        if randint(1,2) == 1:
            img = choice(
                [
                    'WQ.jpg', 'WQ.png', 'WQ2.jpg', 'WQ3.jpg', 'FN.jpg'
                ]
            )
            img = Path('.') / 'ATRI' / 'data' / 'emoji' / f'{img}'
            img = os.path.abspath(img)
            await session.send(f'[CQ:image,file=file:///{img}]')

        elif randint(1,2) == 2:
            res = randint(1,3)
            if res == 1:
                await session.send('对嘴臭人以火箭组合必杀拳，来让他好好喝一壶！哼！')
            
            elif res == 2:
                await session.send('鱼雷组合拳——————————————————啊————！！！')
            
            elif res == 3:
                await session.send('火箭拳——————————————————————————！！！')

@on_command('ciallo', patterns = [r"[Cc][iI][aA][lL][lL][oO]"], only_to_me = False)
async def az(session: CommandSession):
    if randint(1,2) == 1:
        res = randint(1,2)
        if res == 1:
            img = choice(
                [
                    'CIALLO.jpg', 'CIALLO1.jpg', 'CIALLO2.jpg', 'CIALLO3.jpg', 'CIALLO4.jpg', 'CIALLO5.jpg'
                ]
            )
            img = Path('.') / 'ATRI' / 'data' / 'emoji' / f'{img}'
            img = os.path.abspath(img)
            await session.send(f'[CQ:image,file=file:///{img}]')
        
        elif res == 2:
            await session.send('Ciallo～(∠・ω< )⌒★')

@on_command('ne', patterns = [r"呐|ねえ|口内"], only_to_me = False)
async def az(session: CommandSession):
    if randint(1,3) == 1:
        await session.send(
            choice(
                [
                    '呐', '呐呐呐', 'ねえ', 'ねえねえ'
                ]
            )
        )

@on_command('kani', patterns = [r"螃蟹|🦀|カニ|[kK]ani"], only_to_me = False)
async def az(session: CommandSession):
    if random.randint(1,2) == 1:
        img = choice(
            [
                'KN.png', 'KN.jpg', 'KN1.jpg', 'KN2.jpg', 'KN3.png'
            ]
        )
        img = Path('.') / 'ATRI' / 'data' / 'emoji' / f'{img}'
        img = os.path.abspath(img)
        await session.send(f'[CQ:image,file=file:///{img}]')