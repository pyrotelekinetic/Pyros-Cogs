from discord.ext import commands

class Wide:
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def wide(self, ctx, *, msg=""):
        """
        I don't know... It makes the text wide.

        Usage:
        
        [p]wide <a string that you wish to be wide>
            ＮＯＷ　ＹＯＵＲ　ＳＴＲＩＮＧ　ＩＳ　ＷＩＤＥ
            
        [p]wide
            Makes last message in channel wide
            
        [p]wide <message id of message that you wish to be wide>
            ＭＥＳＳＡＧＥ　ＣＯＮＴＥＮＴＳ　ＯＮＬＹ　ＷＩＤＥ
            
        """

        if msg:
            if msg.isdigit():
                async for message in ctx.channel.history(limit=100):
                    if str(message.id) == msg:
                        msg = message.content
                        break
        else:
            switch = False
            async for message in ctx.channel.history(limit=2):
                if switch:
                    msg = message.content
                else:
                    switch = True

        result = ""

        substitution_dict = {
            "A": "Ａ",
            "B": "Ｂ",
            "C": "Ｃ",
            "D": "Ｄ",
            "E": "Ｅ",
            "F": "Ｆ",
            "G": "Ｇ",
            "H": "Ｈ",
            "I": "Ｉ",
            "J": "Ｊ",
            "K": "Ｋ",
            "L": "Ｌ",
            "M": "Ｍ",
            "N": "Ｎ",
            "O": "Ｏ",
            "P": "Ｐ",
            "Q": "Ｑ",
            "R": "Ｒ",
            "S": "Ｓ",
            "T": "Ｔ",
            "U": "Ｕ",
            "V": "Ｖ",
            "W": "Ｗ",
            "X": "Ｘ",
            "Y": "Ｙ",
            "Z": "Ｚ",
            "a": "ａ",
            "b": "ｂ",
            "c": "ｃ",
            "d": "ｄ",
            "e": "ｅ",
            "f": "ｆ",
            "g": "ｇ",
            "h": "ｈ",
            "i": "ｉ",
            "j": "ｊ",
            "k": "ｋ",
            "l": "ｌ",
            "m": "ｍ",
            "n": "ｎ",
            "o": "ｏ",
            "p": "ｐ",
            "q": "ｑ",
            "r": "ｒ",
            "s": "ｓ",
            "t": "ｔ",
            "u": "ｕ",
            "v": "ｖ",
            "w": "ｗ",
            "x": "ｘ",
            "y": "ｙ",
            "z": "ｚ",
            "1": "１",
            "2": "２",
            "3": "３",
            "4": "４",
            "5": "５",
            "6": "６",
            "7": "７",
            "8": "８",
            "9": "９",
            "0": "０",
            "!": "！",
            "?": "？",
            " ": "　"
            }

        result = msg.translate(str.maketrans(substitution_dict))

        await ctx.message.delete()
        await ctx.send(result)

def setup(bot):
	bot.add_cog(Wide(bot))


#Lyric you halp me so much
