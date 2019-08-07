public void processVideos() {
        if (storage.list().size() == 0) {
            throw new NoVideoAvailableException();
        }

        Collections.sort(storage.list(), new Comparator<Advertisement>() {
            @Override
            public int compare(Advertisement o1, Advertisement o2) {
                if (o1.getAmountPerOneDisplaying() > o2.getAmountPerOneDisplaying()) {
                    return -1;
                } else if (o1.getAmountPerOneDisplaying() < o2.getAmountPerOneDisplaying()) {
                    return 1;
                } else {
                    if (o1.getDuration() > o2.getDuration()) {
                        return -1;
                    } else if (o1.getDuration() < o2.getDuration()) {
                        return 1;
                    } else {
                        return 0;
                    }
                }
            }
        });

        List<Advertisement> listToShow = new ArrayList<>();
        int showTime = timeSeconds;
        for (Advertisement ad : storage.list()) {
            if (ad.getHits() > 0) {
                if (showTime - ad.getDuration() >= 0) {
                    listToShow.add(ad);
                    showTime -= ad.getDuration();
                }
            }
        }

        Collections.sort(listToShow, new Comparator<Advertisement>() {
            @Override
            public int compare(Advertisement o1, Advertisement o2) {
                if (o1.getAmountPerOneDisplaying() > o2.getAmountPerOneDisplaying()) {
                    return -1;
                } else if (o1.getAmountPerOneDisplaying() < o2.getAmountPerOneDisplaying()){
                    return 1;
                } else {
                    return secAmountComparing(o1, o2);
                }
            }
        });

        for (Advertisement ad : listToShow) {
            ConsoleHelper.writeMessage(ad.toString());
            ad.revalidate();
        }
}

    private int secAmountComparing(Advertisement o1, Advertisement o2) {
        double firstAdAmount = (o1.getAmountPerOneDisplaying() * 1.0) / (o1.getDuration() * 1.0);
        double secondAdAmount = (o2.getAmountPerOneDisplaying() * 1.0) / (o2.getDuration() * 1.0);

        if (new BigDecimal(firstAdAmount).setScale(3, RoundingMode.DOWN).doubleValue() >
                new BigDecimal(secondAdAmount).setScale(3, RoundingMode.DOWN).doubleValue()) {
            return 1;
        } else if (new BigDecimal(firstAdAmount).setScale(3, RoundingMode.DOWN).doubleValue() <
                new BigDecimal(secondAdAmount).setScale(3, RoundingMode.DOWN).doubleValue()) {
            return -1;
        } else {
            return 0;
        }
    }