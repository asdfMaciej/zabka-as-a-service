for (i in unique(zabka$name)) {
	ggplot(zabka[zabka$name == i,], aes(timeout)) + geom_bar()
	ggsave(paste(i, ".png"))
}