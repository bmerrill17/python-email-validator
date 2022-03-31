from email_validator import validate_email
import pandas as pd

examples = ['firstlast@gmail.', 'firstlast@gmail.com', '@gmail.com']

df = pd.DataFrame({'emails': examples})

df['valid'] = df.apply(lambda x: validate_email(x['emails']).valid, axis=1)
df['errors'] = df.apply(lambda x: validate_email(x['emails']).error, axis=1)

pd.set_option('display.expand_frame_repr', False)

print(df)
