# Translate Dovecot IMAP folders to maildir folders
# - Translate INBOX to "."
# - Prefix a "." to all other folders

def dovecot_nametrans( foldername ):
	if foldername == 'INBOX':
		return '.'
	else:
		return '.' + foldername

# Translate UW IMAP folders to maildir folders
# - Translate INBOX to "."
# - Strip mail/ and prefix a "." to all other folders

def uw_nametrans( foldername ):
	import re
	if foldername == 'INBOX':
		return '.'
	else:
		return re.sub('^mail/', '.', foldername)

# Translate Gmail IMAP folders to maildir folders
# - Translate INBOX to "."
# - Prefix a "." to all other folders
# TODO: What about / in [Gmail]/Drafts?

def gmail_nametrans( foldername ):
	if foldername == 'INBOX':
		return '.'
	else:
		return '.' + foldername
