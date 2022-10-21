def checkperm(user, perm: list) -> bool:
  return any(word in ', '.join([str(p).lower() for p in user.guild_permissions]) for word in perm)
