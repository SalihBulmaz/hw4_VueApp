
<template>
    <table style="width:100%">
        <tbody>
            <tr>
                <td style="background: #ff6600">
                    <table border="0" cellpadding="0" cellspacing="0" width="100%" style="padding:2px">
                        <tbody>
                            <tr>
                                <td style="line-height:12pt; height:10px;"><span class="pagetop"><b class="hnname"><a
                                                href="news">Hacker News | </a></b>
                                        <a href="newswelcome.html">welcome</a> | <a href="newest">new</a> | <a
                                            href="threads?id=hacker_test">threads</a> | <a href="front">past</a> |
                                        <a href="newcomments">comments</a> | <a href="ask">ask</a> | <a
                                            href="show">show</a> | <a href="jobs">jobs</a> | <a href="submit">submit</a>
                                    </span></td>
                                <td style="text-align:right;padding-right:4px;">
                                    <a href="login?goto=news">login</a>
                                </td>
                            </tr>
                        </tbody>
                    </table>
                </td>
            </tr>
        </tbody>
    </table>
</template>
  
<script>
export default {
    name: 'NavBar',
    data: () => ({ }),
}
</script>
  
<style>
a {
    text-decoration: none;
    color: #ffffff!important;
}
</style>