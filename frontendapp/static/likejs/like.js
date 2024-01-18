const dbPromise = idb.openDB('favoritesDB', 1, {
    upgrade(db) {
        db.createObjectStore('favorites');
    }
});

async function toggleFavorite() {
    const heartIcon = document.getElementById('heartIcon');
    const favoriteStatus = document.getElementById('favoriteStatus');

    const db = await dbPromise;
    const tx = db.transaction('favorites', 'readwrite');
    const favoritesStore = tx.objectStore('favorites');

    const isFavorite = await favoritesStore.get('musicc');

    if (isFavorite) {
        await favoritesStore.delete('musicc');
        heartIcon.classList.remove('favorite');
        favoriteStatus.textContent = 'Not Favorited';
    } else {
        await favoritesStore.put('musicc', true);
        heartIcon.classList.add('favorite');
        favoriteStatus.textContent = 'Favorited';
    }

    await tx.complete;
}

window.onload = async function () {
    const heartIcon = document.getElementById('heartIcon');
    const favoriteStatus = document.getElementById('favoriteStatus');

    const db = await dbPromise;
    const favoritesStore = db.transaction('favorites').objectStore('favorites');

    const isFavorite = await favoritesStore.get('musicc');

    if (isFavorite) {
        heartIcon.classList.add('favorite');
        favoriteStatus.textContent = 'Favorited';
    } else {
        heartIcon.classList.remove('favorite');
        favoriteStatus.textContent = 'Not Favorited';
    }
};
