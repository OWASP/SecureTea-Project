from securetea.lib.waf.Server.classifier import WAF

# Train the WAF classifier in case of any error occurs.

train = WAF([None, None, None])
train.train_model()