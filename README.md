val launchIntent =
    packageManager.getLaunchIntentForPackage(
        packageName
    )

launchIntent?.apply {

    addFlags(
        Intent.FLAG_ACTIVITY_NEW_TASK
    )

    addFlags(
        Intent.FLAG_ACTIVITY_REORDER_TO_FRONT
    )

    addFlags(
        Intent.FLAG_ACTIVITY_SINGLE_TOP
    )

    startActivity(this)
}
