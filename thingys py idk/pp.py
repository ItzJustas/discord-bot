@client.command(aliases=["size"])
async def pp(ctx, member: discord.Member, *, reason=None):
    responses = ["8D",
                 "8=D",
                 "8==D",
                 "8===D",
                 "8====D",
                 "8=====D",
                 "8======D",
                 "8=======D",
                 "8========D",
                 "8=========D",
                 "8==========D",
                 "8===========D",
                 "8============D",
                 "8==============D",
                 "8===============D",
                 "8=================D",
                 "8===================D",
                 "8====================D",
                 "8=====================D",
                 "8=======================D",
                 "8=========================D",
                 "8===============================================================================D",
                 "(i)"
                 ]
    await ctx.send(f"{member.mention} {random.choice(responses)}")